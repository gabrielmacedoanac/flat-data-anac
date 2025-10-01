import { table } from "https://deno.land/x/flat@0.0.15/mod.ts";
await (async()=>{
  const r=await fetch("https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/completa.xml?codigoPoder=1&codigoEsfera=1&codigoUnidade=86144&retornarOrgaoEntidadeVinculados=SIM");
  if(!r.ok) throw r.status;
  const x=[...new DOMParser().parseFromString(await r.text(),"application/xml").querySelectorAll("unidades")].map(u=>({
    s:u.querySelector("sigla")?.textContent||"",
    n:u.querySelector("nome")?.textContent||"",
    c:u.querySelector("competencia")?.textContent.replace(/\s+/g," ")||"",
    f:u.querySelector("endereco>uf")?.textContent||"",
    m:u.querySelector("endereco>municipio")?.textContent||"",
    z:u.querySelector("endereco>cep")?.textContent||"",
    i:u.querySelector("codigoUnidade")?.textContent.split("/").pop()||"",
    p:u.querySelector("codigoUnidadePai")?.textContent.split("/").pop()||""
  }));
  x.forEach(u=>{
    let S=[],y=u;
    while(y){S.unshift(y.s||y.n);y=x.find(z=>z.i===y.p)};
    u.siglaCompleta=S.join("/");
    if(u.s.startsWith("NURAC")){
      const a=u.n.split(" ");
      u.s=`NURAC ${a[6]||""} ${a[7]||""}`
    }
  });
  await table(x).save("anac-estrutura.tsv")
})();
