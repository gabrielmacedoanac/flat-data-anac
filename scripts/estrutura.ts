await (async () => {
  const r = await fetch(
    "https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/completa.xml?codigoPoder=1&codigoEsfera=1&codigoUnidade=86144&retornarOrgaoEntidadeVinculados=SIM"
  );
  if (!r.ok) throw r.status;

  const x = [
    ...new DOMParser()
      .parseFromString(await r.text(), "application/xml")
      .querySelectorAll("unidades"),
  ].map((u) => ({
    s: u.querySelector("sigla")?.textContent || "",
    n: u.querySelector("nome")?.textContent || "",
    c: u.querySelector("competencia")?.textContent.replace(/\s+/g, " ") || "",
    f: u.querySelector("endereco>uf")?.textContent || "",
    m: u.querySelector("endereco>municipio")?.textContent || "",
    z: u.querySelector("endereco>cep")?.textContent || "",
    i: u.querySelector("codigoUnidade")?.textContent.split("/").pop() || "",
    p: u.querySelector("codigoUnidadePai")?.textContent.split("/").pop() || "",
  }));

  x.forEach((u) => {
    let S: string[] = [], y = u;
    while (y) {
      S.unshift(y.s || y.n);
      y = x.find((z) => z.i === y.p);
    }
    u.siglaCompleta = S.join("/");
    if (u.s.startsWith("NURAC")) {
      const a = u.n.split(" ");
      u.s = `NURAC ${a[6] || ""} ${a[7] || ""}`;
    }
  });

  const header = [
    "Sigla",
    "Sigla Completa",
    "Nome",
    "Competencia",
    "UF",
    "Municipio",
    "CEP",
    "CodigoUnidade",
    "CodigoUnidadePai",
  ].join("\t");

  const rows = x
    .map((u) =>
      [
        u.s,
        u.siglaCompleta,
        u.n,
        u.c,
        u.f,
        u.m,
        u.z,
        u.i,
        u.p,
      ].join("\t")
    )
    .join("\n");

  await Deno.writeTextFile("anac-estrutura.tsv", `${header}\n${rows}`);
})();
