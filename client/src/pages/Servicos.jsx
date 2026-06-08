import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout"; 
import api from "../services/api"; 
import "./Servicos.css"; 

function Servicos() {
  const navigate = useNavigate();
  
  // 1. Estados
  const [servicos, setServicos] = useState([]);
  const [carregando, setCarregando] = useState(true);

  // 2. Busca ao carregar a página
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

  // 3. Função de Exclusão
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
          onClick={() => navigate("/servicos/novo")}
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
                {/* Ajuste o nome do campo abaixo se no seu Django ele se chamar "nome" em vez de "servico" */}
                <th>Serviço</th> 
                <th>Valor</th>
                <th>Ações</th>
              </tr>
            </thead>
            
            <tbody>
              {servicos.length > 0 ? (
                servicos.map((servico) => (
                  <tr key={servico.id}>
                    <td>{servico.id}</td>
                    {/* Aqui renderizamos os campos reais do banco. Se for 'nome' e 'preco', mude aqui */}
                    <td>{servico.nome || servico.descricao || "-"}</td>
                    <td>{formatarValor(servico.valor || servico.preco || 0)}</td>
                    <td>
                      <button 
                        className="btn-danger"
                        onClick={() => handleDeletar(servico.id)}
                      >
                        Excluir
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