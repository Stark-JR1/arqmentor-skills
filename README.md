# ArqMentor Skills v2

Pacote de teste estável para montar um **Projeto no ChatGPT/GPT** com foco em produção técnica recorrente.

## Objetivo
Evitar retrabalho causado por contexto perdido, decisões improvisadas e entregas sem validação.

## Como montar o Projeto GPT
1. Crie um Projeto chamado `ArqMentor v2 - TESTE`.
2. Cole o conteúdo de `PROJECT_INSTRUCTIONS.md` nas instruções do Projeto.
3. Adicione como arquivos de conhecimento: `AGENTS.md`, `AIZEN_MAP.md`, `TOOL_FALLBACK.md`, `SKILL_REGISTRY.md`, `DECISIONS_TO_CONFIRM.md` e a pasta/ZIP `.agents/skills`.
4. Adicione `tests/ACCEPTANCE_TESTS.md` para validar o ambiente.
5. Use tarefas reais em cópias de arquivos, nunca produção no primeiro ciclo.

## Estrutura
- `PROJECT_INSTRUCTIONS.md`: comportamento principal do Projeto GPT.
- `AGENTS.md`: acordo técnico permanente.
- `AIZEN_MAP.md`: roteamento.
- `.agents/skills/*/SKILL.md`: instruções especializadas.
- `TOOL_FALLBACK.md`: contorno de falhas de ferramenta.
- `tests/`: suíte de aceitação.
- `scripts/`: validadores locais opcionais.
- `templates/`: modelos de relatório.

## Critério de estabilidade v2
A v2 não promete que toda ferramenta estará disponível. Ela exige que o agente:
- detecte limitações;
- use fallback seguro;
- não invente validação;
- preserve originais;
- entregue apenas o que foi efetivamente verificado.

## Primeiro teste recomendado
Use uma cópia de uma planilha real com:
- fórmulas;
- formatação;
- validação de dados;
- área de impressão;
- referências de faixa que precisem ser ampliadas.

O teste passa somente se o arquivo final abrir, mantiver estrutura e nenhuma fórmula crítica ficar quebrada.
