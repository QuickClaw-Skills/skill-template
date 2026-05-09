# skill-template

> Template oficial para criar skills na plataforma QuickClaw.

## Inicio Rapido

1. Clique **"Use this template"** no GitHub para criar seu repo (ex: `skill-minha-coisa`)
2. Atualize `name` em `SKILL.md` (frontmatter) e `skill.json` para o slug do seu repo
3. Atualize `homepage` em `skill.json` para a URL do seu repo
4. Edite `SKILL.md` body com as instrucoes da skill
5. Preencha `RELEASE_NOTES.md` (template ja incluido)
6. Commit, tag `v1.0.0`, push e crie a release no GitHub
7. CI roda automaticamente (skill-ci ja wireado em `.github/workflows/ci.yml`) — sync 3-way obrigatorio

## Estrutura

```
skill-minha-coisa/
├── SKILL.md                       # Instrucoes para o LLM (obrigatorio)
├── skill.json                     # Manifesto (obrigatorio)
├── README.md                      # Documentacao (obrigatorio)
├── LICENSE                        # Licenca (obrigatorio)
├── RELEASE_NOTES.md               # Notas da release atual (template incluido)
├── .gitignore
├── .github/workflows/ci.yml       # skill-ci wireado (obrigatorio)
├── resources/                     # Docs de referencia (opcional)
│   └── *.md
└── workspace/                     # Scripts executaveis (opcional)
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

## CI (skill-ci)

O template ja vem wireado ao `skill-ci` da org. A cada push/PR/tag, o workflow `.github/workflows/ci.yml` chama `QuickClaw-Skills/skill-ci@v1` validando:

- SKILL.md raiz + frontmatter
- skill.json valido + semver
- Sem arquivos/diretorios proibidos (`.env`, `data/`, `tmp/`, `output/`, `__pycache__/`, etc.)
- Sem padroes de segredo (Anthropic/OpenAI/GitHub/Google/AWS/private keys)
- Sem paths absolutos do host
- Syntax check (python/node/bash)
- Sync 3-way em push de tag (`skill.json.version` == tag == release title)

Ver [QuickClaw-Skills/skill-ci](https://github.com/QuickClaw-Skills/skill-ci) para detalhes.

## Releases

**Obrigatorio:** toda skill precisa de releases com tags semver. Playbook normativo em [skill-builder/resources/release-management.md](https://github.com/QuickClaw-Skills/skill-builder/blob/main/resources/release-management.md).

Resumo do fluxo:

```bash
# 1. Bumpar skill.json.version
# 2. Preencher RELEASE_NOTES.md (template ja incluido)
# 3. Commit + tag + push
git add -A && git commit -m "release: vX.Y.Z"
git tag vX.Y.Z
git push origin main --tags

# 4. Criar release
gh release create vX.Y.Z --title "vX.Y.Z" --notes-file RELEASE_NOTES.md
```

CI bloqueia tag se `skill.json.version` nao bater com a tag (sync 3-way).

## Referencia

Para guia completo de criacao/revisao de skills, instale o **skill-builder** no seu agente:
- [QuickClaw-Skills/skill-builder](https://github.com/QuickClaw-Skills/skill-builder)

## Licenca

**Este template e MIT por design** — para permitir que devs copiem livremente como base.

**Skills derivadas DEVEM mudar para `Proprietary`** (politica padrao da org QuickClaw-Skills) ANTES da primeira release:

1. Substituir `LICENSE` pelo arquivo Proprietary padrao da org
2. Atualizar `"license": "Proprietary"` em `skill.json`
3. Atualizar a secao Licenca deste README

Excecoes (skills que devem permanecer abertas como Apache 2.0 / MIT) sao decisao explicita do owner da skill, documentada no commit da release inicial. Politica completa: [skill-builder/resources/skill-standards.md](https://github.com/QuickClaw-Skills/skill-builder/blob/main/resources/skill-standards.md#licenca).
