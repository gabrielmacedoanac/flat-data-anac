import { DOMParser } from "https://deno.land/x/deno_dom/deno-dom-wasm.ts";

const r = await fetch("https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/completa.xml?codigoPoder=1&codigoEsfera=1&codigoUnidade=86144&retornarOrgaoEntidadeVinculados=SIM");
if (!r.ok) throw r.status;

const text = await r.text();
const doc = new DOMParser().parseFromString(text, "text/xml");
if (!doc) throw "Erro ao parsear XML";

const u = [...doc.querySelectorAll("unidades")].map(x => ({
  s: x.querySelector("sigla")?.textContent || "",
  n: x.querySelector("nome")?.textContent || "",
  c: x.querySelector("competencia")?.textContent.replace(/\s+/g," ") || "",
  f: x.querySelector("endereco>uf")?.textContent || "",
  m: x.querySelector("endereco>municipio")?.textContent || "",
  z: x.querySelector("endereco>cep")?.textContent || "",
  i: x.querySelector("codigoUnidade")?.textContent.split("/").pop() || "",
  p: x.querySelector("codigoUnidadePai")?.textContent.split("/").pop() || ""
}));

u.forEach(x=>{
  let S=[], y=x;
  while(y){ S.unshift(y.s||y.n); y=u.find(z=>z.i===y.p); }
  x.siglaCompleta = S.join("/");
  if(x.s.startsWith("NURAC")) {
    const a=x.n.split(" ");
    x.s=`NURAC ${a[6]||""} ${a[7]||""}`;
  }
});

const header=["Sigla","Sigla Completa","Nome","Competencia","UF","Municipio","CEP","CodigoUnidade","CodigoUnidadePai"].join("\t");
const rows=u.map(x=>[x.s,x.siglaCompleta,x.n,x.c,x.f,x.m,x.z,x.i,x.p].join("\t")).join("\n");

await Deno.writeTextFile("anac-estrutura.tsv", `${header}\n${rows}`);
