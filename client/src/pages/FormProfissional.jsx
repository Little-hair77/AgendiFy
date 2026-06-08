import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css";

function FormularioProfissional() {
  const navigate = useNavigate();
  const { id } = useParams(); 
  const isEdicao = Boolean(id); 

  const [nome, setNome] = useState("");
  const [cargo, setCargo] = useState("");
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

  // Busca os dados do profissional
  useEffect(() => {
    if (isEdicao) {
      buscarProfissionalParaEdicao();
    }
  }, [id]);

  const buscarProfissionalParaEdicao = async () => {
    try {
      const resposta = await api.get(`/profissionais/${id}/`);
      const prof = resposta.data;
      setNome(prof.nome || "");
      setCargo(prof.cargo || "");
      // O backend DRF geralmente retorna a ForeignKey como um ID inteiro
      setEmpresaId(prof.empresa || ""); 
    } catch (error) {
      console.error("Erro ao buscar profissional:", error);
      alert("Erro ao carregar os dados. O profissional pode ter sido excluído.");
      navigate("/profissionais");
    } finally {
      setCarregandoDados(false);
    }
  };

  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    const payload = {
      nome: nome,
      cargo: cargo,
      empresa: empresaId
    };

    try {
      if (isEdicao) {
        await api.put(`/profissionais/${id}/`, payload);
        alert("Profissional atualizado com sucesso!");
      } else {
        await api.post("/profissionais/", payload);
        alert("Profissional cadastrado com sucesso!");
      }
      navigate("/profissionais"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao salvar os dados. Verifique as informações.");
    } finally {
      setSalvando(false);
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">{isEdicao ? "Editar Profissional" : "Novo Profissional"}</h1>
      </div>

      <div className="form-container">
        {carregandoDados ? (
          <div style={{ textAlign: "center", padding: "20px", color: "#64748b" }}>
            Carregando dados do profissional...
          </div>
        ) : (
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
                {salvando ? "Salvando..." : isEdicao ? "Salvar Alterações" : "Cadastrar Profissional"}
              </button>
            </div>

          </form>
        )}
      </div>
    </Layout>
  );
}

export default FormularioProfissional;