# Changelog

Todas as mudanças relevantes do projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não publicado]

### Adicionado

- Beta inicial: API FastAPI, ingestão CSV idempotente, KPIs de vendas, dashboard e webhook Shopify assinado.
- Estrutura inicial do repositório (README, AGENTS, CONTRIBUTING, docs, backend, frontend, tests, .github).
- Regras de desenvolvimento para IA e engenharia em `AGENTS.md`.
- Pitch inicial e estrutura documentados no `README.md`.
- Documentação técnica de arquitetura (`docs/architecture/`): visão geral, backend (Python/FastAPI), API, integrações, dados/métricas, frontend, infraestrutura.
- Decisões de arquitetura (ADRs) em `docs/decisions/` (monólito modular, API REST, secrets, Python).
- Regras concretas do backend (Python) em `AGENTS.md` e `backend/README.md`. Documentos de arquitetura referenciados no README.

### Alterado

- Frontend convertido de **React/TypeScript** para um site **estático** (`index.html` + `styles.css` + `app.js`), sem framework nem etapa de build — maior simplicidade e estabilidade. O `app.js` consome a API e renderiza métricas e gráfico no navegador.
- CI do frontend: validação do site estático no lugar de `npm run build`.
