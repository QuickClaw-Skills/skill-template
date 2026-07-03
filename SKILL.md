---
name: skill-template
description: |
  Template oficial QuickClaw para criar skills novas com a estrutura padronizada
  da org: SKILL.md, skill.json, LICENSE, README.md, RELEASE_NOTES.md e CI via
  QuickClaw-Skills/skill-ci. Use quando devs quiserem criar, revisar ou clonar
  uma skill base para publicação na org QuickClaw-Skills. A skill é apenas um
  scaffold e não possui capacidade operacional própria. Ao clonar, substituir
  name, description, keywords e manter licença Proprietary salvo exceção aprovada.
  Keywords: template, scaffold, starter, boilerplate, criar skill, new skill,
  skill QuickClaw, skill-ci, skill-builder, marketplace QuickClaw.
---

# Minha Skill (renomear)

Uma frase que resume o proposito.

## Quando Usar

- Cenario 1: descricao
- Cenario 2: descricao
- Cenario 3: descricao

## Como Funciona

Instrucoes claras em linguagem natural.
Prefira exemplos a explicacoes.

## Formato de Resposta

- Estrutura: bullet points / tabela / paragrafo
- Tom: formal / casual / tecnico
- Idioma: PT-BR
- Comprimento: conciso

## Exemplos

### Exemplo 1: [cenario]
**Usuario:** "mensagem do usuario"
**Bot:** resposta esperada

### Exemplo 2: [cenario]
**Usuario:** "mensagem do usuario"
**Bot:** resposta esperada

## Regras

- NUNCA faca X
- SEMPRE faca Y
- Se Z, entao W

## Contrato de exec (manter SE a skill executa scripts; remover caso contrario)

> Padrao obrigatorio p/ preflight do OpenClaw 5.2x+ — ver `skill-builder/resources/skill-standards.md`.

Para executar o script desta skill, use a ferramenta `exec` com **um unico comando direto**:

```bash
# exec com workdir: ~/.openclaw/skills/<slug-da-skill>
python3 workspace/run.py <argumentos>
```

Alternativa (de qualquer workdir): `python3 ~/.openclaw/skills/<slug-da-skill>/workspace/run.py <argumentos>`

**PROIBIDO no mesmo comando**: `cd ... &&`, `;`, pipes (`|`), redirecionamentos, `source .venv/bin/activate` (o wrapper cuida do venv), `python3 -c "..."`, prefixo de env, subshell.

Se aparecer `exec preflight: complex interpreter invocation detected`: NAO e falta de permissao nem defeito da skill — reexecute na forma direta acima. NUNCA use web_search/web_fetch como fallback de dados.
