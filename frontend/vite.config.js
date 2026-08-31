// CloudOps — servir o site estático em desenvolvimento (HTML/CSS/JS puros).
// Vite aqui atua apenas como servidor estático; não há build nem framework.
import { defineConfig } from "vite";

export default defineConfig({
  server: {
    host: "127.0.0.1",
    port: 5173,
  },
  build: {
    // Sem bundling: o site já é estático. Desabilitar minimiza o que o Vite
    // poderia transformar e mantém os arquivos entregues como estão.
    rollupOptions: {
      input: "index.html",
    },
  },
});
