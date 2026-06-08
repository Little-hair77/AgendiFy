import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api"; 
import "./Empresas.css"; 

function Empresas() {
  const navigate = useNavigate();
  
  const [empresas, setEmpresas] = useState([]);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    carregarEmpresas();
  }, []);

  const carregarEmpresas = async () => {
    try {
      setCarregando(true);
      const resposta = await api.get("/empresas/");
      setEmpresas(resposta.data.results || resposta.data);
    } catch (error) {
      console.error("Erro ao buscar empresas:", error);
      alert("Falha ao carregar a lista de empresas.");
    } finally {
      setCarregando(false);
    }
  };

  const handleDeletar = async (id) => {
    const confirmar = window.confirm("Tem certeza que deseja excluir esta empresa?");
    if (!confirmar) return;

    try {
      await api.delete(`/empresas/${id}/`);
      setEmpresas(empresas.filter((empresa) => empresa.id !== id));
      alert("Empresa excluída com sucesso!");
    } catch (error) {
      console.error("Erro ao deletar:", error);
      alert("Erro ao excluir a empresa. Verifique as permissões.");
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">Empresas</h1>
        <button 
          className="btn-primary"
          onClick={() => navigate("/empresas/cadastrar")}
        >
          + Nova Empresa
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
                <th>E-mail</th>
                <th>Telefone</th>
                <th style={{ textAlign: "center" }}>Ações</th>
              </tr>
            </thead>
            <tbody>
              {empresas.length > 0 ? (
                empresas.map((empresa) => (
                  <tr key={empresa.id}>
                    <td>{empresa.id}</td>
                    <td>{empresa.nome}</td>
                    <td>{empresa.email}</td>
                    <td>{empresa.telefone}</td>
                    <td style={{ display: "flex", justifyContent: "center", gap: "10px" }}>
                      
                      {/* Botão de Edição */}
                      <button 
                        className="btn-icon btn-edit"
                        onClick={() => navigate(`/empresas/editar/${empresa.id}`)}
                        title="Editar Empresa"
                      >
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                          <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                        </svg>
                      </button>

                      {/* Botão de Exclusão */}
                      <button 
                        className="btn-icon btn-danger"
                        onClick={() => handleDeletar(empresa.id)}
                        title="Excluir Empresa"
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
                    Nenhuma empresa cadastrada ainda.
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

export default Empresas;