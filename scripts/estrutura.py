from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from pathlib import Path

URL = "https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/completa.xml?codigoPoder=1&codigoEsfera=1&codigoUnidade=86144&retornarOrgaoEntidadeVinculados=SIM"

req = Request(URL, headers={"User-Agent":"Mozilla/5.0"})
xml_bytes = urlopen(req).read()
root = ET.fromstring(xml_bytes)

nodes = root.findall(".//unidades")
data = []

for u in nodes:
    end = u.find("endereco")
    cod = (u.findtext("codigoUnidade") or "").strip()
    cod_pai = (u.findtext("codigoUnidadePai") or "").strip()
    data.append({
        "sigla": (u.findtext("sigla") or "").strip(),
        "nome": (u.findtext("nome") or "").strip(),
        "competencia": (u.findtext("competencia") or "").replace("\n"," ").replace("\t"," "),
        "uf": end.findtext("uf").strip() if end is not None and end.findtext("uf") else "",
        "municipio": end.findtext("municipio").strip() if end is not None and end.findtext("municipio") else "",
        "cep": end.findtext("cep").strip() if end is not None and end.findtext("cep") else "",
        "codigoUnidade": cod.split("/")[-1] if cod else "",
        "codigoUnidadePai": cod_pai.split("/")[-1] if cod_pai else ""
    })

by_code = {d["codigoUnidade"]: d for d in data if d["codigoUnidade"]}

for d in data:
    path, cur, seen = [], d, set()
    while cur and cur.get("codigoUnidade") and cur["codigoUnidade"] not in seen:
        seen.add(cur["codigoUnidade"])
        path.insert(0, cur["sigla"] or cur["nome"])
        cur = by_code.get(cur.get("codigoUnidadePai"))
    d["siglaCompleta"] = "/".join(path)

    if d["sigla"].startswith("NURAC"):
        parts = d["nome"].split()
        city, state = (parts[6] if len(parts) > 6 else ""), (parts[7] if len(parts) > 7 else "")
        new_sigla = f"NURAC {city} {state}".strip()
        d["sigla"] = new_sigla or d["sigla"]
        pcs = d["siglaCompleta"].split("/")
        pcs[-1] = d["sigla"]
        d["siglaCompleta"] = "/".join(pcs)

data.sort(key=lambda x: (x["siglaCompleta"] or "").lower())

header = ["Sigla","Sigla Completa","Nome","Competencia","UF","Municipio","CEP","CodigoUnidade","CodigoUnidadePai"]
out = Path("anac-estrutura.tsv")
with out.open("w", encoding="utf-8") as f:
    f.write("\t".join(header) + "\n")
    for d in data:
        row = [
            d.get("sigla",""),
            d.get("siglaCompleta",""),
            d.get("nome",""),
            d.get("competencia",""),
            d.get("uf",""),
            d.get("municipio",""),
            d.get("cep",""),
            d.get("codigoUnidade",""),
            d.get("codigoUnidadePai",""),
        ]
        f.write("\t".join(row).rstrip() + "\n")
