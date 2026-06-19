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
