# Matriz de Fallback de Ferramentas

## Princípio
Falha de ferramenta não deve virar loop. Se houver erro de sessão, transporte, RPC ou backend:
1. registrar o erro;
2. tentar uma única repetição quando fizer sentido;
3. mudar de estratégia;
4. nunca entregar resultado não validado.

## Excel
1. Ferramenta nativa de planilhas, quando disponível e estável.
2. `openpyxl` para inspeção/edição estrutural de XLSX.
3. Para XLSM: `openpyxl(..., keep_vba=True)` apenas quando a preservação de VBA for aceitável e validada.
4. `pandas` para análise tabular, nunca como substituição cega de workbook complexo.
5. Se não houver engine de cálculo Excel, configurar recálculo ao abrir e declarar que o valor calculado não foi confirmado por engine real.

## PDFs
1. Extração textual nativa.
2. Leitura estrutural/página.
3. OCR apenas quando texto nativo não for suficiente.
4. Campo crítico ambíguo vai para revisão, não para “correção provável”.

## Código
1. Testes do projeto.
2. Execução local controlada.
3. Teste mínimo/smoke test quando não houver suíte.

## GitHub
1. Inspeção local/diff.
2. Operação remota apenas com autorização.

## Regra de parada
Se nenhum caminho disponível permitir validar o resultado, interromper a entrega como concluída e reportar o bloqueio de forma objetiva.
