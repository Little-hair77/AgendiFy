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
    // Confirmação de segurança
    const confirmar = window.confirm("Tem certeza que deseja excluir esta empresa?");
    if (!confirmar) return;

    try {
      await api.delete(`/empresas/${id}/`);
      // Atualiza a lista na tela removendo a empresa deletada sem precisar recarregar a página
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
                <th>CNPJ</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {empresas.length > 0 ? (
                empresas.map((empresa) => (
                  <tr key={empresa.id}>
                    <td>{empresa.id}</td>
                    <td>{empresa.nome}</td>
                    <td>{empresa.cnpj}</td>
                    <td>
                      <button 
                        className="btn-danger"
                        onClick={() => handleDeletar(empresa.id)}
                      >
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" style={{ textAlign: "center", padding: "30px", color: "#64748b" }}>
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