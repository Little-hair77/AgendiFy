import { useState, useEffect } from "react";
import Layout from "../components/Layout"; 
import api from "../services/api";
import "./Dashboard.css"; 

function Dashboard() {
  const [totais, setTotais] = useState({
    empresas: 0,
    profissionais: 0,
    servicos: 0
  });
  
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    async function carregarDados() {
      try {
        const [respEmpresas, respProfissionais, respServicos] = await Promise.all([
          api.get("/empresas/"),
          api.get("/profissionais/"),
          api.get("/servicos/")
        ]);

        setTotais({
          empresas: respEmpresas.data.length || respEmpresas.data.count || 0,
          profissionais: respProfissionais.data.length || respProfissionais.data.count || 0,
          servicos: respServicos.data.length || respServicos.data.count || 0,
        });
      } catch (error) {
        console.error("Erro ao buscar dados do painel:", error);
      } finally {
        setCarregando(false);
      }
    }

    carregarDados();
  }, []);

  return (
    <Layout>
      <div className="dashboard-header">
        <h1>Painel de Controle</h1>
        <p>Visão geral do sistema AgendiFy</p>
      </div>

      <div className="stats-grid">
        
        {/* Card Empresas */}
        <div className="stat-card">
          <div className="stat-icon companies-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect>
              <path d="M9 22v-4h6v4"></path>
              <path d="M8 6h.01"></path>
              <path d="M16 6h.01"></path>
              <path d="M12 6h.01"></path>
              <path d="M12 10h.01"></path>
              <path d="M12 14h.01"></path>
              <path d="M16 10h.01"></path>
              <path d="M16 14h.01"></path>
              <path d="M8 10h.01"></path>
              <path d="M8 14h.01"></path>
            </svg>
          </div>
          <div className="stat-info">
            <h3>Empresas</h3>
            <h2>{carregando ? "..." : totais.empresas}</h2>
          </div>
        </div>

        {/* Card Profissionais */}
        <div className="stat-card">
          <div className="stat-icon professionals-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
          </div>
          <div className="stat-info">
            <h3>Profissionais</h3>
            <h2>{carregando ? "..." : totais.profissionais}</h2>
          </div>
        </div>

        {/* Card Serviços */}
        <div className="stat-card">
          <div className="stat-icon services-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect>
              <line x1="8" y1="12" x2="16" y2="12"></line>
              <line x1="8" y1="16" x2="16" y2="16"></line>
              <line x1="8" y1="8" x2="16" y2="8"></line>
            </svg>
          </div>
          <div className="stat-info">
            <h3>Serviços</h3>
            <h2>{carregando ? "..." : totais.servicos}</h2>
          </div>
        </div>

      </div>
    </Layout>
  );
}

export default Dashboard;