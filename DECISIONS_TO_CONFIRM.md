# Decisões que exigem confirmação

Confirmar antes de:
- sobrescrever/excluir arquivo original quando houver risco de perda;
- alterar regra de negócio sem evidência suficiente;
- converter PBIX/PBIP quando isso mudar fluxo de trabalho;
- executar UPDATE/DELETE destrutivo ou em produção;
- push, merge, release, exclusão remota ou reescrita de histórico Git;
- executar compra, pagamento, envio externo ou ação irreversível;
- aceitar OCR incerto em CNPJ, valores, linha digitável, NF, patrimônio ou número de série;
- alterar/remover macro VBA;
- substituir fórmulas por valores;
- descartar dados como “duplicados” sem chave/regra confirmada;
- mudar arquitetura de sistema apenas para facilitar implementação.

Não exigir confirmação para:
- criar cópia de trabalho;
- gerar diagnóstico;
- corrigir erro inequívoco em cópia;
- criar teste, log ou relatório de validação;
- aplicar formatação técnica coerente sem alterar significado.
