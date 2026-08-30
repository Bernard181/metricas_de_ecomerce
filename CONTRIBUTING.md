# Contribuindo para o CloudOps

Obrigado pelo interesse em contribuir com o CloudOps. Este guia descreve como participar do projeto de forma organizada, seguindo as regras definidas em [AGENTS.md](AGENTS.md).

## Fluxo de trabalho

```
GitHub Issue
    ↓
Implementação
    ↓
Testes
    ↓
Pull Request
    ↓
Revisão
    ↓
MERGE
```

## Começando

1. Leia o [README.md](README.md) para entender o projeto.
2. Consulte o [AGENTS.md](AGENTS.md) para as regras de desenvolvimento.
3. Crie uma Issue descrevendo o problema ou melhoria.

## Branches

Nunca trabalhe diretamente na `main`. Sempre crie uma branch a partir da `main`:

```
feature/nome-da-feature
fix/nome-do-bug
refactor/nome-da-alteracao
docs/nome-da-documentacao
```

## Commits

Commits devem ser pequenos e descritivos, seguindo o padrão de prefixo:

- `feat:` — nova funcionalidade
- `fix:` — correção de bug
- `refactor:` — refatoração
- `docs:` — documentação
- `test:` — testes
- `build:` / `chore:` — manutenção

Exemplos:

```
feat: add metrics endpoint
fix: validate metric payload
refactor: simplify alert service
```

## Pull Requests

Alterações relevantes devem passar por Pull Request. O PR deve explicar:

- o que mudou;
- por que mudou;
- como foi testado;
- possíveis riscos.

## Critérios de aceitação

Uma contribuição só é considerada completa quando:

- resolução de um único problema (respeitando a regra de escopo);
- código segue a arquitetura do projeto;
- possui testes criados/atualizados e passando;
- sem secrets ou dados sensíveis;
- documentação atualizada quando necessário;
- PR revisado;
- changelog atualizado quando necessário.
