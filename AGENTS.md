# CloudOps — AI Development Rules

## Sobre o projeto

CloudOps é uma plataforma de inteligência operacional.

Lema:
> "Inteligência para cada operação."

## Objetivo

Construir uma plataforma capaz de transformar dados operacionais em métricas, insights e alertas. Gerenciar e orquestrar todo o seu negócio acompanhando cada métrica — quanto mais você conhece o próprio negócio, melhor você o gerencia.

> Know your business. Run it better.

---

# Regras de desenvolvimento

## 1. Antes de modificar

Sempre:

- entender a arquitetura existente;
- procurar código relacionado;
- consultar documentação;
- verificar testes existentes.

## 2. Código

- Não reescrever componentes sem necessidade.
- Não criar dependências sem justificar.
- Manter funções pequenas.
- Priorizar simplicidade.
- Não duplicar lógica.

## 3. Segurança

Nunca:

- expor secrets;
- colocar tokens no código;
- modificar autenticação sem revisão;
- ignorar validações.

## 4. Testes

Toda nova funcionalidade deve possuir testes.

Não considerar uma tarefa concluída somente porque o código executa.

## 5. Git

Nunca trabalhar diretamente na `main`.

Utilizar branches:

- `feature/`
- `fix/`
- `refactor/`

## 6. Commits

Commits devem ser pequenos e descritivos.

Exemplos:

- `feat: add metrics endpoint`
- `fix: validate metric payload`
- `docs: update architecture`

## 7. Documentação

Alterações arquiteturais importantes devem ser documentadas em `/docs`.

## 8. IA

A IA deve:

- explicar alterações importantes;
- declarar incertezas;
- não inventar requisitos;
- não alterar arquivos desnecessários;
- seguir este documento.

---

# CloudOps Engineering Rules

## 1. Princípio fundamental

Priorize simplicidade, clareza e manutenção. Não criar complexidade que não seja necessária para resolver o problema atual.

## 2. Arquitetura

O projeto deve separar:

- API
- domínio
- regras de negócio
- serviços
- persistência
- infraestrutura.

A camada de API não deve conter regras de negócio complexas. Regras de negócio devem permanecer independentes de frameworks sempre que possível.

## 3. Responsabilidade

Cada módulo deve possuir uma responsabilidade clara.

Evitar:

- funções gigantes;
- classes com múltiplas responsabilidades;
- código duplicado;
- dependências desnecessárias.

Preferir componentes pequenos e reutilizáveis.

## 4. Desenvolvimento

Antes de modificar código:

1. entender o problema;
2. procurar implementação existente;
3. verificar arquitetura;
4. verificar testes;
5. modificar somente o necessário.

Não reescrever partes do sistema sem necessidade.

## 5. Novas funcionalidades

Toda nova funcionalidade deve possuir:

- objetivo claro;
- critérios de aceitação;
- implementação;
- testes;
- documentação quando necessário.

Evitar implementar várias funcionalidades em uma única alteração.

## 6. Testes

Código novo deve possuir testes.

Prioridade:

1. regras de negócio;
2. serviços;
3. APIs críticas;
4. integrações.

Um código não é considerado concluído apenas porque executou uma vez.

## 7. Segurança

Nunca:

- colocar secrets no código;
- colocar tokens no Git;
- ignorar validação de entrada;
- confiar cegamente em dados externos;
- expor informações internas.

Toda entrada externa deve ser considerada não confiável.

## 8. Dependências

Antes de adicionar uma biblioteca:

- verificar se já existe solução no projeto;
- avaliar necessidade;
- avaliar manutenção;
- avaliar impacto.

Não adicionar dependências apenas por conveniência.

## 9. Git

Nunca trabalhar diretamente na `main` para funcionalidades ou correções relevantes.

Usar:

```
feature/nome-da-feature
fix/nome-do-bug
refactor/nome-da-alteracao
```

Commits devem ser pequenos e descritivos.

Exemplos:

- `feat: add metrics endpoint`
- `fix: validate metric payload`
- `refactor: simplify alert service`
- `docs: update architecture`

## 10. Pull Request

Alterações relevantes devem passar por Pull Request.

O PR deve explicar:

- o que mudou;
- por que mudou;
- como foi testado;
- possíveis riscos.

## 11. Documentação

Documentar:

- decisões arquiteturais;
- mudanças importantes;
- APIs relevantes;
- comportamentos não óbvios.

Não documentar código trivial apenas para aumentar a quantidade de documentação.

## 12. IA

Agentes de IA devem:

- seguir este documento;
- consultar o código existente;
- não inventar requisitos;
- não alterar arquivos desnecessários;
- explicar mudanças importantes;
- informar incertezas;
- executar testes após alterações.

A IA não deve assumir decisões estratégicas.

## 13. Regra de ouro

Se uma solução simples resolve o problema, não utilizar uma solução complexa.

Preferir:

> "funciona, é testável e é fácil de entender"

a:

> "é sofisticado, mas difícil de manter."

---

# Regras técnicas do backend (Python)

> Referência rápida do agente. Detalhes em [`docs/architecture/backend.md`](docs/architecture/backend.md).

- **Linguagem: Python 3.12+**. Stack: FastAPI, Pydantic v2, SQLAlchemy 2 + Alembic, PostgreSQL, Redis (fila RQ/ARQ), pytest, ruff.
- **Arquitetura hexagonal**: `api → application → domain → infrastructure`. Regras de negócio (`domain`) são puras, sem framework.
- **Todo código comentado e tipado**: docstrings em funções públicas, comentários de intenção (o *porquê*), type hints em todas as assinaturas. Isso é obrigatório para produtividade e manutenção.
- Camadas: `app/api` (routers/schemas), `app/application` (casos de uso), `app/domain` (entidades/regras/ports), `app/integrations` (connectors), `app/infrastructure` (db/fila/cache/http), `app/shared`.
- Integrações: cada fonte é um connector isolado; timeout, retry (tenacity), circuit breaker; idempotência via chave `{source}+{external_id}`; falha de uma fonte não afeta as demais.
- API: REST versao `/api/v{n}`, contrato OpenAPI (automático no FastAPI), JWT, erros padronizados (ver [`docs/architecture/api.md`](docs/architecture/api.md)).
- Sempre consultar [`docs/architecture/`](docs/architecture/) antes de implementar.

---

# Documentos de arquitetura

Índice e detalhes em [`docs/architecture/README.md`](docs/architecture/README.md): visão geral, backend (Python), API, integrações, dados/métricas, frontend e infraestrutura. Decisões arquiteturais em [`docs/decisions/`](docs/decisions/).

---

# Regra de escopo

Uma tarefa deve resolver um problema.

Não aproveitar uma tarefa para realizar refatorações não relacionadas.

Se uma melhoria for descoberta durante o trabalho, registrá-la como nova Issue.

---

# Fluxo de trabalho

Modelo simples:

```
GitHub Issue
    ↓
OpenCode/Codex
    ↓
Implementação
    ↓
Testes
    ↓
Pull Request
    ↓
Você revisa
    ↓
MERGE
```

---

# Definition of Done

Uma tarefa só está concluída quando:

- [ ] Implementação concluída
- [ ] Código segue arquitetura
- [ ] Testes criados/atualizados
- [ ] Testes passando
- [ ] Sem secrets ou dados sensíveis
- [ ] Documentação atualizada quando necessário
- [ ] Pull Request revisado
- [ ] Alterações relacionadas não foram misturadas
- [ ] Issue atualizada
- [ ] Changelog atualizado quando necessário
