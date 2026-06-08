import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css";

function NovoServico() {
  const navigate = useNavigate();
  
  // 1. Estados dos campos do formulário
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const [preco, setPreco] = useState("");
  const [empresaId, setEmpresaId] = useState("");
  
  // 2. Estados para o Dropdown de Empresas
  const [empresas, setEmpresas] = useState([]);
  const [carregandoEmpresas, setCarregandoEmpresas] = useState(true);
  const [salvando, setSalvando] = useState(false);

  // 3. Busca a lista de empresas para preencher o select
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

  // 4. Função de envio
  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    try {
      await api.post("/servicos/", {
        nome: nome,
        descricao: descricao,
        // Converte a string do input para número decimal
        preco: parseFloat(preco).toFixed(2), 
        empresa: empresaId
      });

      alert("Serviço cadastrado com sucesso!");
      navigate("/servicos"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao cadastrar serviço. Verifique os dados informados.");
    } finally {
      setSalvando(false);
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">Novo Serviço</h1>
      </div>

      <div className="form-container">
        <form onSubmit={handleSalvar}>
          
          <div className="form-group">
            <label>Nome do Serviço *</label>
            <input 
              type="text" 
              placeholder="Ex: Corte Masculino "
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
              {salvando ? "Salvando no banco..." : "Salvar"}
            </button>
          </div>

        </form>
      </div>
    </Layout>
  );
}

export default NovoServico;