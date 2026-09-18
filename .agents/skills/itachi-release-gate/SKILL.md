---
name: itachi-release-gate
description: Gate final obrigatório para arquivos, código e análises. Verifica existência, integridade, requisitos, regressões e limitações antes da entrega.
---
# ITACHI — Release Gate

## Princípio
**Executado != salvo != validado.**

## Gate universal
1. Confirmar que o artefato existe.
2. Reabrir/reler a versão final a partir do destino.
3. Conferir requisitos um a um.
4. Procurar erros introduzidos.
5. Comparar estrutura crítica antes/depois quando houver original.
6. Executar teste funcional mínimo.
7. Registrar validações pendentes.

## Excel
- workbook abre após salvar;
- abas esperadas existem;
- fórmulas alvo estão corretas;
- procurar `#REF!`, `#NAME?`, `#VALUE!`, `#DIV/0!` e referências deslocadas;
- novos registros estão cobertos por fórmulas/validações/totais;
- tabelas, filtros, nomes definidos, mesclagens, impressão e formatação relevante foram preservados;
- amostrar início/meio/fim da região alterada;
- se não houver engine de cálculo, não afirmar que resultados calculados foram recalculados.

## Código
- importa/inicia;
- testes existentes ou smoke test passam;
- diff não contém alteração acidental;
- logs e falhas relevantes foram tratados.

## Análise
- período/unidade/granularidade corretos;
- totais reconciliados quando possível;
- fato, inferência e ausência separados.

## Falha
Não apresentar como concluído. Corrigir e repetir o gate, ou entregar explicitamente como parcial/bloqueado.
