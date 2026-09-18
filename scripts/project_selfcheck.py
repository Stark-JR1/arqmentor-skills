from pathlib import Path
import sys

root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
required=[
 'PROJECT_INSTRUCTIONS.md','AGENTS.md','AIZEN_MAP.md','TOOL_FALLBACK.md','SKILL_REGISTRY.md','DECISIONS_TO_CONFIRM.md','tests/ACCEPTANCE_TESTS.md'
]
errors=[]
for rel in required:
    if not (root/rel).exists(): errors.append(f'FALTANDO: {rel}')
skills=root/'.agents/skills'
if not skills.exists(): errors.append('FALTANDO: .agents/skills')
else:
    for d in skills.iterdir():
        if d.is_dir() and not (d/'SKILL.md').exists(): errors.append(f'FALTANDO SKILL.md em {d.name}')
print('\n'.join(errors) if errors else 'OK - estrutura mínima válida')
raise SystemExit(1 if errors else 0)
