## v2.2.0 - 2026-08-07

## Wrapper de referencia com propagacao de exit code

> Bump: MINOR
> Compatibilidade: adicao. Skill criada da versao anterior nao precisa de acao.

### Added
- `workspace/run.py` — wrapper de referencia para skill com entrypoint Python. Ja nasce propagando o exit code do processo filho e avisando no stderr quando degrada para o Python global.
- README: secao explicando as duas regras e quando apagar `workspace/`.

### Why
Skill nova nao herdava o defeito do template (ele nao tinha wrapper nenhum) — herdava de copy-paste das skills irmas, e cinco delas descartavam o exit code. Wrapper que engole a falha do filho faz o bot tratar erro como sucesso. Agora o ponto de partida esta correto, e o `skill-ci` v1.5.0+ reprova quem se desviar.

### Validation
- [x] Passa no `check-wrapper-exit-code` do skill-ci; removendo a linha de propagacao, o check reprova (verificado nas duas direcoes).
- [x] skill-ci local: 7 validacoes verdes.

Version bump: v2.1.0 -> v2.2.0.

## v2.1.0 - 2026-07-03

## Bloco "Contrato de exec" pronto no template

- SKILL.md do template ganha secao "Contrato de exec" pre-preenchida (manter se a skill executa scripts, remover caso contrario) — padrao do preflight OpenClaw 5.2x+ (Bug 76).

## v2.0.3 - 2026-07-01

## Release workflow

- Added the canonical reusable QuickClaw Skills release workflow.
- Keeps future GitHub releases aligned with skill-ci automation.

Version bump: v2.0.2 -> v2.0.3.

## v2.0.2 — 2026-06-19

- Align template manifest license with QuickClaw-Skills Proprietary default.
- Expand SKILL.md frontmatter description for better trigger quality and policy clarity.

## v2.0.1 — 2026-06-17

> Bump: PATCH sobre a linha v2
> Compatibilidade: mantém o template simples alinhado ao skill-builder v2 e corrige o sync release/tag/manifest.

### Changed
- `skill.json.version` alinhado para `2.0.1`, preservando as melhorias atuais de template e evitando regressao para a linha `1.0.x`.
- `PROJECT.md` adicionado para registrar versao, tag, release e regra operacional do template.

### Fixed
- Corrige desalinhamento em que a tag mais alta era `v2.0.0`, mas `skill.json` e latest release ainda apontavam `v1.0.1`.
- Evita mover ou sobrescrever a tag historica `v2.0.0`; a correcao passa a ser publicada como `v2.0.1`.

### Validation
- [x] `python3 -m json.tool skill.json`
- [x] `git diff --check`
