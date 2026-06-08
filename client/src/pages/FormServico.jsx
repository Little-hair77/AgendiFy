import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css";

function FormularioServico() {
  const navigate = useNavigate();
  const { id } = useParams(); 
  const isEdicao = Boolean(id); 
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const [preco, setPreco] = useState("");
  const [empresaId, setEmpresaId] = useState("");
  
  const [empresas, setEmpresas] = useState([]);
  const [carregandoEmpresas, setCarregandoEmpresas] = useState(true);
  const [carregandoDados, setCarregandoDados] = useState(isEdicao);
  const [salvando, setSalvando] = useState(false);

  useEffect(() => {
    async function buscarEmpresas() {
      try {
        const resposta = await api.get("/empresas/");
        setEmpresas(resposta.data.results || resposta.data);
      } catch (error) {
        console.error("Erro ao buscar empresas:", error);
        alert("Não foi possível carregar a lista de empresas.");
      } finally {
        setCarregandoEmpresas(false);
      }
    }
    
    buscarEmpresas();
  }, []);

  useEffect(() => {
    if (isEdicao) {
      buscarServicoParaEdicao();
    }
  }, [id]);

  const buscarServicoParaEdicao = async () => {
    try {
      const resposta = await api.get(`/servicos/${id}/`);
      const serv = resposta.data;
      setNome(serv.nome || "");
      setDescricao(serv.descricao || "");
      setPreco(serv.preco || ""); 
      setEmpresaId(serv.empresa || "");
    } catch (error) {
      console.error("Erro ao buscar serviço:", error);
      alert("Erro ao carregar os dados. O serviço pode ter sido excluído.");
      navigate("/servicos");
    } finally {
      setCarregandoDados(false);
    }
  };

  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    const payload = {
      nome: nome,
      descricao: descricao,
      preco: parseFloat(preco).toFixed(2), 
      empresa: empresaId
    };

    try {
      if (isEdicao) {
        // Modo Edição (PUT)
        await api.put(`/servicos/${id}/`, payload);
        alert("Serviço atualizado com sucesso!");
      } else {
        // Modo Criação (POST)
        await api.post("/servicos/", payload);
        alert("Serviço cadastrado com sucesso!");
      }
      navigate("/servicos"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao salvar o serviço. Verifique os dados informados.");
    } finally {
      setSalvando(false);
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">{isEdicao ? "Editar Serviço" : "Novo Serviço"}</h1>
      </div>

      <div className="form-container">
        {carregandoDados ? (
          <div style={{ textAlign: "center", padding: "20px", color: "#64748b" }}>
            Carregando dados do serviço...
          </div>
        ) : (
          <form onSubmit={handleSalvar}>
            
            <div className="form-group">
              <label>Nome do Serviço *</label>
              <input 
                type="text" 
                placeholder="Ex: Corte Masculino Degradê"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                required
              />
            </div>

            <div className="form-group">
              <label>Preço (R$) *</label>
              <input 
                type="number" 
                step="0.01" 
                min="0"
                placeholder="0.00"
                value={preco}
                onChange={(e) => setPreco(e.target.value)}
                required
              />
            </div>

            <div className="form-group">
              <label>Empresa Vinculada *</label>
              <select
                value={empresaId}
                onChange={(e) => setEmpresaId(e.target.value)}
                required
                disabled={carregandoEmpresas}
                style={{
                  width: "100%",
                  padding: "12px 16px",
                  borderRadius: "8px",
                  border: "1px solid #e2e8f0",
                  backgroundColor: "#f8fafc",
                  fontSize: "1rem",
                  color: "#1e293b",
                  cursor: carregandoEmpresas ? "wait" : "pointer"
                }}
              >
                <option value="" disabled>
                  {carregandoEmpresas ? "Carregando empresas..." : "Selecione uma empresa"}
                </option>
                
                {empresas.map((emp) => (
                  <option key={emp.id} value={emp.id}>
                    {emp.nome}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Descrição Detalhada</label>
              <textarea 
                placeholder="Descreva o que está incluso neste serviço..."
                value={descricao}
                onChange={(e) => setDescricao(e.target.value)}
                rows="4"
                style={{
                  width: "100%",
                  padding: "12px 16px",
                  borderRadius: "8px",
                  border: "1px solid #e2e8f0",
                  backgroundColor: "#f8fafc",
                  fontSize: "1rem",
                  fontFamily: "inherit",
                  resize: "vertical"
                }}
              />
            </div>

            <div className="form-actions">
              <button 
                type="button" 
                className="btn-cancel"
                onClick={() => navigate("/servicos")}
              >
                Cancelar
              </button>
              
              <button 
                type="submit" 
                className="btn-submit"
                disabled={salvando || carregandoEmpresas}
              >
                {salvando ? "Salvando..." : isEdicao ? "Salvar Alterações" : "Cadastrar"}
              </button>
            </div>

          </form>
        )}
      </div>
    </Layout>
  );
}

export default FormularioServico;