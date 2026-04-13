# skill-template

> Template oficial para criar skills na plataforma QuickClaw.

## Inicio Rapido

1. Clique **"Use this template"** no GitHub para criar seu repo
2. Renomeie `minha-skill` para o nome da sua skill (em todos os arquivos)
3. Edite `SKILL.md` com as instrucoes da skill
4. Edite `skill.json` com os metadados
5. Crie a release `v1.0.0` no GitHub

## Estrutura

```
minha-skill/
├── SKILL.md          # Instrucoes para o LLM (obrigatorio)
├── skill.json        # Manifesto (obrigatorio)
├── README.md         # Documentacao (obrigatorio)
├── LICENSE           # Licenca (obrigatorio)
├── .gitignore
├── resources/        # Docs de referencia (opcional)
│   └── *.md
└── workspace/        # Scripts executaveis (opcional)
    └── *.sh, *.py
```

## Arquivos Obrigatorios

| Arquivo | Proposito |
|---------|-----------|
| `SKILL.md` | Instrucoes para o LLM — frontmatter com name + description |
| `skill.json` | Manifesto — versao, dependencias, permissoes, tags |
| `README.md` | Documentacao para devs/users — features, exemplos, changelog |
| `LICENSE` | Licenca da skill |

## Skill Simples vs Pack

**Este template e para skill simples** (1 skill = 1 repo, SKILL.md na raiz).

Para **packs** (multiplas sub-skills num repo), use estrutura com `skills/`:
```
skill-pack/
├── skill.json
├── skills/
│   ├── sub-skill-1/SKILL.md
│   └── sub-skill-2/SKILL.md
├── workspace/    # SOUL.md, AGENTS.md (compartilhado)
└── config/       # openclaw.json (compartilhado)
```

## Releases

**Obrigatorio:** toda skill precisa de releases com tags semver.

```bash
git tag v1.0.0
git push origin main --tags
gh release create v1.0.0 --title "v1.0.0" --notes "Release inicial"
```

## Referencia

Para guia completo de criacao de skills, instale o **skill-builder** no seu agente:
- [QuickClaw-Skills/skill-builder](https://github.com/QuickClaw-Skills/skill-builder)

## Licenca

MIT — use como base para sua skill.
