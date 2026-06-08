import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout"; 
import api from "../services/api"; 
// Importação do CSS Empresa para estilização de botões
import "./Empresas.css"; 

function Profissionais() {
  const navigate = useNavigate();
  
  const [profissionais, setProfissionais] = useState([]);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    carregarProfissionais();
  }, []);

  const carregarProfissionais = async () => {
    try {
      setCarregando(true);
      const resposta = await api.get("/profissionais/");
      setProfissionais(resposta.data.results || resposta.data);
    } catch (error) {
      console.error("Erro ao buscar profissionais:", error);
      alert("Falha ao carregar a lista de profissionais.");
    } finally {
      setCarregando(false);
    }
  };

  const handleDeletar = async (id) => {
    const confirmar = window.confirm("Tem certeza que deseja excluir este profissional?");
    if (!confirmar) return;

    try {
      await api.delete(`/profissionais/${id}/`);
      setProfissionais(profissionais.filter((prof) => prof.id !== id));
      alert("Profissional excluído com sucesso!");
    } catch (error) {
      console.error("Erro ao deletar:", error);
      alert("Erro ao excluir. Verifique as permissões.");
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">Profissionais</h1>
        <button 
          className="btn-primary"
          onClick={() => navigate("/profissionais/cadastrar")}
        >
          + Novo Profissional
        </button>
      </div>

      <div className="table-container">
        {carregando ? (
          <div className="loading-state">Buscando dados no servidor...</div>
        ) : (
          <table className="data-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Cargo</th>
                <th>Status</th>
                <th style={{ textAlign: "center" }}>Ações</th>
              </tr>
            </thead>
            
            <tbody>
              {profissionais.length > 0 ? (
                profissionais.map((profissional) => (
                  <tr key={profissional.id}>
                    <td>{profissional.id}</td>
                    <td>{profissional.nome}</td>
                    <td>{profissional.cargo || "-"}</td>
                    <td>
                      <span style={{
                        padding: "4px 8px",
                        borderRadius: "12px",
                        fontSize: "0.8rem",
                        fontWeight: "600",
                        backgroundColor: profissional.ativo ? "rgba(34, 197, 94, 0.1)" : "rgba(239, 68, 68, 0.1)",
                        color: profissional.ativo ? "#16a34a" : "#ef4444"
                      }}>
                        {profissional.ativo ? "Ativo" : "Inativo"}
                      </span>
                    </td>
                    <td style={{ display: "flex", justifyItems: "center", justifyContent: "center", gap: "10px" }}>
                      
                      {/* Botão de Edição */}
                      <button 
                        className="btn-icon btn-edit"
                        onClick={() => navigate(`/profissionais/editar/${profissional.id}`)}
                        title="Editar Profissional"
                      >
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                          <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                        </svg>
                      </button>

                      {/* Botão de Exclusão */}
                      <button 
                        className="btn-icon btn-danger"
                        onClick={() => handleDeletar(profissional.id)}
                        title="Excluir Profissional"
                      >
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <polyline points="3 6 5 6 21 6"></polyline>
                          <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                          <line x1="10" y1="11" x2="10" y2="17"></line>
                          <line x1="14" y1="11" x2="14" y2="17"></line>
                        </svg>
                      </button>

                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" style={{ textAlign: "center", padding: "30px", color: "#64748b" }}>
                    Nenhum profissional cadastrado ainda.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        )}
      </div>
    </Layout>
  );
}

export default Profissionais;