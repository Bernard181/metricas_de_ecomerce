# ESTUDO: KPIs de e-commerce para o CloudOps

> **Status:** Rascunho de pesquisa — alimentará o roadmap de negócio e o engine de métricas.
> Ver [`docs/architecture/data-layer.md`](../architecture/data-layer.md).

## Objetivo

Identificar os KPIs mais relevantes para operações de e-commerce e produtos digitais, servindo de base para o modelo de métricas da plataforma.

## Funis principais

### 1. Funil de vendas

- **Impressões** → quantas vezes os anúncios/produtos foram vistos.
- **Cliques / Visitas** → tráfego para a página.
- **Sessões** → visitas únicas.
- **Pedidos** → compras confirmadas.
- **Receita** → valor total vendido.
- **Ticket médio** = receita / pedidos.
- **Conversão** = pedidos / sessões.

### 2. Aquisição de clientes

- **Novos clientes** → primeiro pedido.
- **Custo de aquisição (CAC)** = gasto marketing / novos clientes.
- **ROAS (Return on Ad Spend)** = receita / gasto em anúncio.
- **Custo por clique (CPC) / CPA**.

### 3. Operação e estoque

- **Estoque atual / disponível**.
- **Vendas por produto** → top sellers.
- **Ruptura de estoque** (esgotados).
- **Margem** e **custo por pedido**.

### 4. Financeiro

- **Lucro bruto / líquido**.
- **Margem**.
- **Chargebacks / reembolsos**.

## Próximos passos

- Priorizar o primeiro conjunto mínimo de KPIs (MVP).
- Definir fórmulas exatas e unidades em consenso de negócio.
- Modelar como métricas no engine (ver `data-layer.md`).

> **Atenção para o agente:** este é um documento de pesquisa — não implementar métricas ainda sem a priorização de negócio definida.
