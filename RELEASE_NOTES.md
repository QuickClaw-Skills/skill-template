## v1.0.1 — 2026-05-09

> Bump: PATCH
> Compatibilidade: nenhuma quebra. Apenas description expandida.

### Changed
- `SKILL.md` frontmatter `description` expandida de ~169 chars para ~600 chars. Agora descreve explicitamente: (1) que e template oficial QuickClaw, (2) que se clona via "Use this template" no GitHub, (3) o que vem na estrutura, (4) que skill nao tem capacidade operacional propria, (5) instrucoes de o que devs DEVEM substituir antes da primeira release. Plus keywords bilingues mais completas (template, scaffold, starter, boilerplate, etc.).

### Fixed
- Reaudit (09/05/2026) classificou skill-template como P2 "description curta demais para bom trigger". Resolvido — agora >= 200 chars conforme recomendacao do auditor.

### Validation
- [x] CI da org passa (skill-ci v1.2.1)
- [x] skill.json.version 1.0.0 -> 1.0.1
