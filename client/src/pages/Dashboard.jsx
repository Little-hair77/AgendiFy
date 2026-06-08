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
        <div className="stat-card">
          <div className="stat-icon companies-icon">🏢</div>
          <div className="stat-info">
            <h3>Empresas</h3>
            <h2>{carregando ? "..." : totais.empresas}</h2>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon professionals-icon">👩‍⚕️</div>
          <div className="stat-info">
            <h3>Profissionais</h3>
            <h2>{carregando ? "..." : totais.profissionais}</h2>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon services-icon">📅</div>
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