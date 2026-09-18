---
name: excel-workbook-engineer
description: Cria, corrige e audita XLSX/XLSM/CSV preservando compatibilidade Microsoft 365, fórmulas, layout, impressão e estruturas existentes. Obrigatória quando planilha é entrada ou saída principal.
---
# Excel Workbook Engineer

## Objetivo
Preservação + funcionamento + validação. Formatação bonita com lógica quebrada é falha.

## Fase 1 — Inspeção antes de editar
Mapear quando aplicável:
- extensão e presença de VBA;
- abas visíveis/ocultas;
- dimensões reais e última linha útil;
- fórmulas e padrões por coluna;
- tabelas/AutoFilter;
- nomes definidos;
- validações de dados;
- formatação condicional;
- células mescladas;
- congelamentos;
- gráficos/imagens quando relevantes;
- áreas de impressão, orientação, margens e quebras;
- links externos;
- intervalos fixos (`$3:$102`) incompatíveis com crescimento.

## Fase 2 — Diagnóstico
- identificar causa raiz;
- comparar fórmulas vizinhas para detectar deslocamento;
- distinguir dado digitado de fórmula;
- não assumir que célula vazia é erro;
- não remover estrutura porque a biblioteca não a entende.

## Fase 3 — Estratégia de ferramenta
Seguir `TOOL_FALLBACK.md`.
- `openpyxl` é preferível para editar workbook existente quando compatível.
- `pandas` é ótimo para análise/transformação tabular, não para regravar workbook complexo inteiro.
- XLSM exige preservação consciente de VBA.
- Não usar uma biblioteca que destrua recurso crítico conhecido.

## Fase 4 — Edição
- alterar somente o necessário;
- copiar padrões de fórmula/estilo a partir de linha válida quando seguro;
- preferir Tabelas/intervalos dinâmicos quando isso não muda a arquitetura do usuário;
- não converter fórmula em valor;
- preservar locale/funções do Excel quando necessário;
- não sobrescrever original por padrão.

## Fase 5 — Recálculo
Bibliotecas Python normalmente não calculam fórmulas como o Excel.
Quando não houver engine real:
- marcar workbook para recálculo automático ao abrir quando suportado;
- não usar valor em cache antigo como prova de correção;
- declarar limitação no gate.

## Fase 6 — Validação obrigatória
- salvar em novo arquivo;
- reabrir o arquivo salvo;
- auditar fórmulas/referências;
- comparar abas, dimensões e propriedades críticas;
- testar início/meio/fim da faixa alterada;
- verificar áreas de impressão e validações relevantes;
- acionar ITACHI.

## Protocolo de falha
Se backend/ferramenta retornar BrokenPipe/RPC/transport:
- não repetir em loop;
- tentar no máximo uma repetição razoável;
- migrar para fallback;
- se não houver caminho confiável, interromper como bloqueado.
