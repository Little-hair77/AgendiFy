import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout"; 
import api from "../services/api"; 
import "./Profissionais.css"; 

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
                {/* O nome do campo pode variar no seu models.py */}
                <th>Cargo / Especialidade</th>
                <th>Ações</th>
              </tr>
            </thead>
            
            <tbody>
              {profissionais.length > 0 ? (
                profissionais.map((profissional) => (
                  <tr key={profissional.id}>
                    <td>{profissional.id}</td>
                    <td>{profissional.nome}</td>
                    {/* Renderiza 'cargo' ou 'especialidade' */}
                    <td>{profissional.cargo || profissional.especialidade || "-"}</td>
                    <td>
                      <button 
                        className="btn-danger"
                        onClick={() => handleDeletar(profissional.id)}
                      >
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" style={{ textAlign: "center", padding: "30px", color: "#64748b" }}>
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