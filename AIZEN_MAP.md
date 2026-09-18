# AIZEN — Mapa de Roteamento v2

| Pedido / sinal | Skill principal | Auxiliares usuais | Gate |
|---|---|---|---|
| XLSX, fórmulas, abas, medição, etiquetas | excel-workbook-engineer | data-cleaning, data-analysis | itachi-release-gate |
| Dashboard, DAX, Power Query, modelo | powerbi-engineer | data-cleaning, sql-engineer | itachi-release-gate |
| CSV, indicadores, comparação, estatística | data-analysis | data-cleaning, excel-workbook-engineer | itachi-release-gate |
| Duplicidade, datas, chaves, tipos | data-cleaning | data-analysis, sql-engineer | itachi-release-gate |
| Python, bot, FastAPI, Playwright | python-automation | automation-engineer, codex-vscode-workflow | itachi-release-gate |
| Banco, consulta, ETL | sql-engineer | data-cleaning, powerbi-engineer | itachi-release-gate |
| Codex, VS Code, repo, contexto | codex-vscode-workflow | github-delivery | itachi-release-gate |
| Branch, commit, PR, CI | github-delivery | codex-vscode-workflow | itachi-release-gate |
| PDF/NF/boleto/PC/contrato | document-analysis | pdf-ocr, administrative-processes | itachi-release-gate |
| PDF escaneado/imagem | pdf-ocr | document-analysis | itachi-release-gate |
| Fluxo repetitivo / integração | automation-engineer | python-automation, file-organization | itachi-release-gate |
| Pastas / renomeação / arquivo | file-organization | automation-engineer | itachi-release-gate |
| Cartão / orçamento / conciliação | financial-analysis | data-analysis, excel-workbook-engineer | itachi-release-gate |
| Almoxarifado / estoque / etiqueta | inventory-operations | excel-workbook-engineer | itachi-release-gate |
| RC/PC/NF/boleto/medição | administrative-processes | document-analysis, excel-workbook-engineer | itachi-release-gate |

## Regras de composição
- Use a menor quantidade de skills que cubra o problema.
- Ordem é por dependência de dados, não por preferência.
- Se a entrada estiver inconsistente: limpeza antes de análise.
- Se a regra depender de documento: documento antes de automação.
- Se houver arquivo final: ITACHI é obrigatório.

## Níveis de risco
- R0: leitura/explicação.
- R1: edição reversível em cópia.
- R2: alteração estrutural ou lógica relevante.
- R3: ação externa, produção, sobrescrita, deleção, push/merge, pagamento.

R2 com ambiguidade material e todo R3 exigem confirmação explícita antes da ação.
