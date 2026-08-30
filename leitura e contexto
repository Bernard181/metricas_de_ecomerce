voce open code vai ler todo esse repositorio e fazer nele as seguinetes mudanças dicsirtas abaixo transforme o repositorio em exatamente isso 
cloudops/
│
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── CHANGELOG.md
│
├── docs/
│   ├── architecture/
│   ├── decisions/
│   └── research/
│
├── backend/
├── frontend/
├── tests/
│
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
implemente esse texto onde mais se encaaixar # CloudOps - AI Development Rules

## Sobre o projeto

CloudOps é uma plataforma de inteligência operacional.

Lema:
"Inteligência para cada operação."

## Objetivo

Construir uma plataforma capaz de transformar
dados operacionais em métricas, insights e alertas.

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

Não considerar uma tarefa concluída
somente porque o código executa.

## 5. Git

Nunca trabalhar diretamente na main.

Utilizar branches:

feature/
fix/
refactor/

## 6. Commits

Commits devem ser pequenos e descritivos.

Exemplo:

feat: add metrics endpoint

fix: validate metric payload

docs: update architecture

## 7. Documentação

Alterações arquiteturais importantes devem
ser documentadas em /docs.

## 8. IA

A IA deve:

- explicar alterações importantes;
- declarar incertezas;
- não inventar requisitos;
- não alterar arquivos desnecessários;
- seguir este documento.
modelo simples para ajudar IDEIA
 ↓
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
outr estrutura recomendada 
cloudops/
│
├── AGENTS.md
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
│
├── src/
│   ├── api/
│   ├── core/
│   ├── domain/
│   ├── services/
│   ├── repositories/
│   └── infrastructure/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── docs/
│   ├── architecture/
│   └── decisions/
│
└── .github/
    └── workflows/

# CloudOps Engineering Rules

## 1. PRINCÍPIO FUNDAMENTAL

Priorize simplicidade, clareza e manutenção.

Não criar complexidade que não seja necessária
para resolver o problema atual.

---

## 2. ARQUITETURA

O projeto deve separar:

- API
- domínio
- regras de negócio
- serviços
- persistência
- infraestrutura.

A camada de API não deve conter regras de negócio complexas.

Regras de negócio devem permanecer independentes
de frameworks sempre que possível.

---

## 3. RESPONSABILIDADE

Cada módulo deve possuir uma responsabilidade clara.

Evitar:

- funções gigantes;
- classes com múltiplas responsabilidades;
- código duplicado;
- dependências desnecessárias.

Preferir componentes pequenos e reutilizáveis.

---

## 4. DESENVOLVIMENTO

Antes de modificar código:

1. entender o problema;
2. procurar implementação existente;
3. verificar arquitetura;
4. verificar testes;
5. modificar somente o necessário.

Não reescrever partes do sistema sem necessidade.

---

## 5. NOVAS FUNCIONALIDADES

Toda nova funcionalidade deve possuir:

- objetivo claro;
- critérios de aceitação;
- implementação;
- testes;
- documentação quando necessário.

Evitar implementar várias funcionalidades
em uma única alteração.

---

## 6. TESTES

Código novo deve possuir testes.

Prioridade:

1. regras de negócio;
2. serviços;
3. APIs críticas;
4. integrações.

Um código não é considerado concluído
apenas porque executou uma vez.

---

## 7. SEGURANÇA

Nunca:

- colocar secrets no código;
- colocar tokens no Git;
- ignorar validação de entrada;
- confiar cegamente em dados externos;
- expor informações internas.

Toda entrada externa deve ser considerada não confiável.

---

## 8. DEPENDÊNCIAS

Antes de adicionar uma biblioteca:

- verificar se já existe solução no projeto;
- avaliar necessidade;
- avaliar manutenção;
- avaliar impacto.

Não adicionar dependências apenas por conveniência.

---

## 9. GIT

Nunca trabalhar diretamente na `main`
para funcionalidades ou correções relevantes.

Usar:

feature/nome-da-feature
fix/nome-do-bug
refactor/nome-da-alteracao

Commits devem ser pequenos e descritivos.

Exemplos:

feat: add metrics endpoint
fix: validate metric payload
refactor: simplify alert service
docs: update architecture

---

## 10. PULL REQUEST

Alterações relevantes devem passar por Pull Request.

O PR deve explicar:

- o que mudou;
- por que mudou;
- como foi testado;
- possíveis riscos.

---

## 11. DOCUMENTAÇÃO

Documentar:

- decisões arquiteturais;
- mudanças importantes;
- APIs relevantes;
- comportamentos não óbvios.

Não documentar código trivial apenas para aumentar
a quantidade de documentação.

---

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

---

## 13. REGRA DE OURO

Se uma solução simples resolve o problema,
não utilizar uma solução complexa.

Preferir:

"funciona, é testável e é fácil de entender"

a:

"é sofisticado, mas difícil de manter."
siga tambem ## REGRA DE ESCOPO

Uma tarefa deve resolver um problema.

Não aproveitar uma tarefa para realizar
refatorações não relacionadas.

Se uma melhoria for descoberta durante o trabalho,
registrá-la como nova Issue.
# Definition of Done

Uma tarefa só está concluída quando:

[ ] Implementação concluída

[ ] Código segue arquitetura

[ ] Testes criados/atualizados

[ ] Testes passando

[ ] Sem secrets ou dados sensíveis

[ ] Documentação atualizada quando necessário

[ ] Pull Request revisado

[ ] Alterações relacionadas não foram misturadas

[ ] Issue atualizada

[ ] Changelog atualizado quando necessário
