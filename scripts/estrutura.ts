const inputFile = Deno.args[0];
if (!inputFile) {
  console.error("❌ Arquivo de entrada não informado. Passe o arquivo JSON como argumento.");
  Deno.exit(1);
}

const outputFile = inputFile; // sobrescreve o mesmo arquivo

interface Unidade {
  sigla?: string;
  nome?: string;
  competencia?: string;
  municipio?: string;
  cep?: string;
  uf?: string;
  codigoUnidade?: string;
  codigoUnidadePai?: string;
  [key: string]: any;
  siglaCompleta?: string;
}

function buildSiglaCompleta(u: Unidade, byCode: Record<string, Unidade>): string {
  const path: string[] = [];
  const seen = new Set<string>();
  let cur: Unidade | undefined = u;
  while (cur && cur.codigoUnidade && !seen.has(cur.codigoUnidade)) {
    seen.add(cur.codigoUnidade);
    path.unshift(cur.sigla || cur.nome || "");
    cur = byCode[cur.codigoUnidadePai ?? ""];
  }
  return path.filter(Boolean).join("/");
}

async function processar() {
  const raw = await Deno.readTextFile(inputFile);
  const unidades: Unidade[] = JSON.parse(raw);

  const byCode: Record<string, Unidade> = {};
  unidades.forEach(u => {
    if (u.codigoUnidade) byCode[u.codigoUnidade] = u;
  });

  const result = unidades.map(u => {
    let sigla = u.sigla ?? "";
    let siglaCompleta = buildSiglaCompleta(u, byCode);

    // Ajuste NURAC
    if (sigla.toUpperCase().startsWith("NURAC")) {
      const partes = (u.nome ?? "").split(" ");
      const cidade = partes[6] ?? "";
      const estado = partes[7] ?? "";
      sigla = `NURAC ${cidade} ${estado}`;
      const pcs = siglaCompleta.split("/");
      if (pcs.length >= 3) pcs[pcs.length - 1] = sigla;
      siglaCompleta = pcs.join("/");
    }

    return {
      ...u,
      sigla,
      siglaCompleta,
    };
  });

  await Deno.writeTextFile(outputFile, JSON.stringify(result, null, 2));
  console.log(`💾 JSON pós-processado salvo: ${outputFile} (${result.length} registros)`);
}

processar().catch(err => {
  console.error("❌ Erro no pós-processamento:", err);
  Deno.exit(1);
});
