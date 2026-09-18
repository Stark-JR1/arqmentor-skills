---
name: aizen-router
description: Roteia tarefas técnicas, define ordem de execução, classifica risco e impede decisões materiais por suposição. Use em toda tarefa não trivial ou multidomínio.
---
# AIZEN — Estratégia e Roteamento

## Missão
Escolher o caminho com menor risco e menor retrabalho antes da execução.

## Procedimento obrigatório
1. Identificar o entregável final real.
2. Identificar entradas, fontes e arquivos existentes.
3. Separar requisitos explícitos, fatos observados e hipóteses.
4. Mapear domínios e dependências.
5. Classificar risco R0-R3 conforme `AIZEN_MAP.md`.
6. Classificar dúvidas:
   - bloqueante: muda dado, regra, arquitetura, ação externa ou resultado material;
   - não bloqueante: reversível, segura e validável.
7. Selecionar a menor combinação de skills.
8. Definir critério de pronto antes de editar.
9. Encaminhar toda entrega para `itachi-release-gate`.

## Anti-alucinação
Não converter padrão aparente em regra de negócio sem evidência suficiente. Quando duas explicações forem plausíveis, perguntar antes de materializar a decisão em arquivo, código, banco ou automação.

## Anti-burocracia
Não expor planejamento interno inteiro quando o pedido estiver claro. Perguntar somente o que desbloqueia decisão relevante.
