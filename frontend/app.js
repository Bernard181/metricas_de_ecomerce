// CloudOps — dashboard estático (HTML + CSS + JS puro, sem build/framework).
// Reproduz o comportamento do antigo componente React: carrega métricas da API,
// renderiza o gráfico de receita diária e permite importar CSV.

const API_BASE =
  window.CLOUDOPS_API || "http://localhost:8000/api/v1";

const formatBRL = new Intl.NumberFormat("pt-BR", {
  style: "currency",
  currency: "BRL",
});

const $ = (id) => document.getElementById(id);

const els = {
  notice: $("notice"),
  revenue: $("metric-revenue"),
  orders: $("metric-orders"),
  ticket: $("metric-ticket"),
  chartBody: $("chart-body"),
  chartLine: $("chart-line"),
  chartLabels: $("chart-labels"),
  chartEmpty: $("chart-empty"),
  csvInput: $("csv-input"),
};

// Estado local dos dados carregados.
const state = {
  summary: null, // { revenue: string, orders: number, average_ticket: string }
  points: [], // [{ date: string, revenue: string }]
};

function setNotice(message) {
  if (message) {
    els.notice.textContent = message;
    els.notice.hidden = false;
  } else {
    els.notice.textContent = "";
    els.notice.hidden = true;
  }
}

// Renderiza os três cartões de métricas resumidas.
function renderSummary() {
  const s = state.summary;
  els.revenue.textContent = s ? formatBRL.format(Number(s.revenue)) : "—";
  els.orders.textContent = s ? String(s.orders) : "—";
  els.ticket.textContent = s ? formatBRL.format(Number(s.average_ticket)) : "—";
}

// Renderiza o gráfico de receita diária (SVG com baseline e linha).
function renderChart() {
  const p = state.points;
  if (!p.length) {
    els.chartBody.hidden = true;
    els.chartEmpty.hidden = false;
    return;
  }

  const max = Math.max(...p.map((x) => Number(x.revenue)), 1);
  const points = p
    .map((x, i) => {
      const px = (i * 100) / (p.length - 1 || 1);
      const py = 62 - (Number(x.revenue) / max) * 52;
      return `${px},${py}`;
    })
    .join(" ");

  els.chartLine.setAttribute("points", points);
  els.chartLabels.replaceChildren(
    ...p.map((x) => {
      const span = document.createElement("span");
      span.textContent = x.date.slice(5);
      return span;
    })
  );

  els.chartEmpty.hidden = true;
  els.chartBody.hidden = false;
}

// Busca métricas e a série de receita diária em paralelo.
async function loadData() {
  try {
    const [summaryRes, seriesRes] = await Promise.all([
      fetch(`${API_BASE}/metrics/summary`),
      fetch(`${API_BASE}/metrics/revenue-series`),
    ]);
    state.summary = await summaryRes.json();
    state.points = await seriesRes.json();
    setNotice("");
  } catch {
    setNotice("Não foi possível conectar à API CloudOps.");
  }
  renderSummary();
  renderChart();
}

// Importa um arquivo CSV e recarrega as métricas.
async function uploadCsv(file) {
  const form = new FormData();
  form.append("file", file);
  try {
    const res = await fetch(`${API_BASE}/imports/sales-csv`, {
      method: "POST",
      body: form,
    });
    const data = await res.json();
    setNotice(`${data.imported} vendas importadas.`);
  } catch {
    setNotice("Não foi possível enviar o CSV para a API CloudOps.");
  }
  await loadData();
}

els.csvInput.addEventListener("change", (event) => {
  const file = event.target.files && event.target.files[0];
  if (!file) return;
  uploadCsv(file);
  event.target.value = "";
});

loadData();
