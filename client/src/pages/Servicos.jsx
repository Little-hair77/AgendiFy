import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout"; 
import api from "../services/api"; 
// Importação do CSS Empresa para estilização de botões
import "./Empresas.css"; 

function Servicos() {
  const navigate = useNavigate();
  
  const [servicos, setServicos] = useState([]);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    carregarServicos();
  }, []);

  const carregarServicos = async () => {
    try {
      setCarregando(true);
      const resposta = await api.get("/servicos/");
      setServicos(resposta.data.results || resposta.data);
    } catch (error) {
      console.error("Erro ao buscar serviços:", error);
      alert("Falha ao carregar a lista de serviços.");
    } finally {
      setCarregando(false);
    }
  };

  const handleDeletar = async (id) => {
    const confirmar = window.confirm("Tem certeza que deseja excluir este serviço?");
    if (!confirmar) return;

    try {
      await api.delete(`/servicos/${id}/`);
      setServicos(servicos.filter((servico) => servico.id !== id));
      alert("Serviço excluído com sucesso!");
    } catch (error) {
      console.error("Erro ao deletar:", error);
      alert("Erro ao excluir. Verifique as permissões.");
    }
  };

  // 4. Formatador de Moeda (Transforma 30 em R$ 30,00)
  const formatarValor = (valor) => {
    return new Intl.NumberFormat("pt-BR", {
      style: "currency",
      currency: "BRL",
    }).format(valor);
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">Serviços</h1>
        <button 
          className="btn-primary"
          onClick={() => navigate("/servicos/cadastrar")}
        >
          + Novo Serviço
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
                <th>Serviço</th> 
                <th>Valor</th>
                <th style={{ textAlign: "center" }}>Ações</th>
              </tr>
            </thead>
            
            <tbody>
              {servicos.length > 0 ? (
                servicos.map((servico) => (
                  <tr key={servico.id}>
                    <td>{servico.id}</td>
                    <td>{servico.nome || servico.descricao || "-"}</td>
                    <td>{formatarValor(servico.preco || servico.valor || 0)}</td>
                    <td style={{ display: "flex", justifyItems: "center", justifyContent: "center", gap: "10px" }}>
                      
                      {/* Botão de Edição */}
                      <button 
                        className="btn-icon btn-edit"
                        onClick={() => navigate(`/servicos/editar/${servico.id}`)}
                        title="Editar Serviço"
                      >
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                          <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                        </svg>
                      </button>

                      {/* Botão de Exclusão */}
                      <button 
                        className="btn-icon btn-danger"
                        onClick={() => handleDeletar(servico.id)}
                        title="Excluir Serviço"
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
                  <td colSpan="4" style={{ textAlign: "center", padding: "30px", color: "#64748b" }}>
                    Nenhum serviço cadastrado ainda.
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

export default Servicos;