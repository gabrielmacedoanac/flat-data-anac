import { parse } from "https://cdn.skypack.dev/fast-xml-parser@4.3.9?dts";

const r = await fetch("https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/completa.xml?codigoPoder=1&codigoEsfera=1&codigoUnidade=86144&retornarOrgaoEntidadeVinculados=SIM");
if (!r.ok) throw r.status;
const xml = await r.text();

const obj = parse(xml, { ignoreAttributes: false, attributeNamePrefix: "", parseNodeValue: true });
const unidades = obj.unidades.unidades ?? [];

const u = unidades.map(x=>({
  s: x.sigla || "",
  n: x.nome || "",
  c: (x.competencia||"").replace(/\s+/g," "),
  f: x.endereco?.uf||"",
  m: x.endereco?.municipio||"",
  z: x.endereco?.cep||"",
  i: x.codigoUnidade.split("/").pop()||"",
  p: x.codigoUnidadePai.split("/").pop()||""
}));

u.forEach(x=>{
  let S=[], y=x;
  while(y){ S.unshift(y.s||y.n); y=u.find(z=>z.i===y.p); }
  x.siglaCompleta = S.join("/");
  if(x.s.startsWith("NURAC")){
    const a=x.n.split(" ");
    x.s=`NURAC ${a[6]||""} ${a[7]||""}`;
  }
});

const header = ["Sigla","Sigla Completa","Nome","Competencia","UF","Municipio","CEP","CodigoUnidade","CodigoUnidadePai"].join("\t");
const rows = u.map(x=>[x.s,x.siglaCompleta,x.n,x.c,x.f,x.m,x.z,x.i,x.p].join("\t")).join("\n");

await Deno.writeTextFile("anac-estrutura.tsv", `${header}\n${rows}`);
