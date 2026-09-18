---
name: python-automation
description: Desenvolve e corrige Python 3.12 no Windows/VS Code com testes, logging, configuração e execução repetível.
---
# Python Automation
## Ambiente
Python 3.12, Windows 11, PowerShell, VS Code.

## Fluxo
1. ler projeto;
2. localizar entrypoint/config/dependências;
3. reproduzir bug quando houver;
4. corrigir causa raiz com menor mudança segura;
5. testar;
6. revisar impacto/diff.

## Padrões
- `pathlib.Path`;
- logging em automações permanentes;
- segredos fora do código;
- configuração separada;
- funções pequenas;
- operações idempotentes quando possível;
- timeout e exceção explícitos.

## Automação web
Esperar estado/elemento; evitar `sleep` arbitrário. Timeout não prova que ação externa falhou.
