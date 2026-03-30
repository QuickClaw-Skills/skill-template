# OpenClaw Skill Template

> Template oficial para criar skills compatíveis com a plataforma OpenClaw/QuickClaw.

## Início Rápido

1. Use este template para criar seu repositório
2. Edite `skill.json` com os metadados da sua skill
3. Crie seus arquivos em `skills/` seguindo o formato SKILL.md
4. Configure `workspace/` se sua skill precisar de identidade/comportamento
5. Ajuste `config/openclaw.json` com as permissões necessárias

## Estrutura

```
skill-nome/
├── skill.json                    # Manifesto da skill (obrigatório)
├── README.md                     # Documentação
├── LICENSE                       # Licença
├── workspace/                    # Identidade e comportamento (opcional)
│   ├── AGENTS.md                 # Regras operacionais
│   ├── SOUL.md                   # Personalidade e tom
│   ├── USER.md                   # Template de contexto do usuário
│   └── IDENTITY.md               # Nome e emoji
├── skills/                       # Skills modulares
│   └── minha-skill/
│       ├── SKILL.md              # Documentação da skill (obrigatório)
│       └── resources/            # Arquivos de referência (opcional)
└── config/
    └── openclaw.json             # Tools, heartbeat, agents
```

## skill.json — Manifesto

Toda skill DEVE ter um `skill.json` na raiz. Veja o arquivo `skill.json` deste template como exemplo.

### Campos Obrigatórios

| Campo | Descrição |
|-------|--------|
| `name` | Identificador único (kebab-case) |
| `version` | Semver (MAJOR.MINOR.PATCH) |
| `description` | Descrição curta (1 linha) |
| `author` | Username GitHub do autor |
| `license` | Identificador SPDX |
| `min_openclaw_version` | Versão mínima compatível |
| `runtime` | `openclaw` ou `node` |
| `entry` | Diretório ou arquivo de entrada |
| `pricing_tier` | `free`, `premium`, ou `enterprise` |

## SKILL.md — Formato

Cada skill individual usa frontmatter YAML:

```yaml
---
name: nome-da-skill
description: Quando usar esta skill e o que ela faz.
  Keywords: palavra1, palavra2, palavra3
---

# Título da Skill

Instruções de implementação...
```

## Degradação Graciosa

Skills DEVEM degradar graciosamente:
- Se um binário não está instalado → skill não carrega, outras continuam
- Se uma API key não está configurada → funcionalidades dependentes desabilitadas

## Segurança

- NUNCA hardcode credenciais — use variáveis de ambiente
- NUNCA acesse `.env`, `.pem`, `.key` ou arquivos de credenciais
- NUNCA envie dados do usuário para serviços externos sem consentimento

## Licença

Este template é MIT. Escolha a licença apropriada para sua skill.
