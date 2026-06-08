import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css";

function NovoProfissional() {
  const navigate = useNavigate();
  
  const [nome, setNome] = useState("");
  const [cargo, setCargo] = useState("");
  const [empresaId, setEmpresaId] = useState(""); 
  
  // 2. Estados para o Dropdown de Empresas
  const [empresas, setEmpresas] = useState([]);
  const [carregandoEmpresas, setCarregandoEmpresas] = useState(true);
  const [salvando, setSalvando] = useState(false);

  useEffect(() => {
    async function buscarEmpresas() {
      try {
        const resposta = await api.get("/empresas/");
        // Extrai a lista corretamente, lidando com a paginação do DRF caso exista
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

  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    try {
      await api.post("/profissionais/", {
        nome: nome,
        cargo: cargo,
        empresa: empresaId // O Django espera receber o ID da ForeignKey
      });

      alert("Profissional cadastrado com sucesso!");
      navigate("/profissionais"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao cadastrar profissional. Verifique os dados.");
    } finally {
      setSalvando(false);
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">Novo Profissional</h1>
      </div>

      <div className="form-container">
        <form onSubmit={handleSalvar}>
          
          <div className="form-group">
            <label>Nome do Profissional *</label>
            <input 
              type="text" 
              placeholder="Ex: Higo Alves"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Cargo / Especialidade</label>
            <input 
              type="text" 
              placeholder="Ex: Barbeiro Sênior"
              value={cargo}
              onChange={(e) => setCargo(e.target.value)}
            />
          </div>

          {/* Dropdown Dinâmico para a Chave Estrangeira (ForeignKey) */}
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

          <div className="form-actions">
            <button 
              type="button" 
              className="btn-cancel"
              onClick={() => navigate("/profissionais")}
            >
              Cancelar
            </button>
            
            <button 
              type="submit" 
              className="btn-submit"
              disabled={salvando || carregandoEmpresas}
            >
              {salvando ? "Salvando no banco..." : "Salvar "}
            </button>
          </div>

        </form>
      </div>
    </Layout>
  );
}

export default NovoProfissional;