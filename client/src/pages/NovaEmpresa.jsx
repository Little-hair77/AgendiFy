import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css"; 

function NovaEmpresa() {
  const navigate = useNavigate();
  
  const [nome, setNome] = useState("");
  const [cnpj, setCnpj] = useState("");
  const [salvando, setSalvando] = useState(false);

  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    try {
      // Manda os dados para a API do Django
      await api.post("/empresas/", {
        nome: nome,
        cnpj: cnpj
      });

      alert("Empresa cadastrada com sucesso!");
      // Volta para a tabela de listagem
      navigate("/empresas"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao cadastrar empresa. Verifique os dados.");
    } finally {
      setSalvando(false);
    }
  };

  return (
    <Layout>
      <div className="page-header">
        <h1 className="page-title">Nova Empresa</h1>
      </div>

      <div className="form-container">
        <form onSubmit={handleSalvar}>
          
          <div className="form-group">
            <label>Nome da Empresa</label>
            <input 
              type="text" 
              placeholder="Ex: Barbearia do Higo"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>CNPJ</label>
            <input 
              type="text" 
              placeholder="00.000.000/0000-00"
              value={cnpj}
              onChange={(e) => setCnpj(e.target.value)}
              required
            />
          </div>

          <div className="form-actions">
            <button 
              type="button" 
              className="btn-cancel"
              onClick={() => navigate("/empresas")}
            >
              Cancelar
            </button>
            
            <button 
              type="submit" 
              className="btn-submit"
              disabled={salvando}
            >
              {salvando ? "Salvando no banco..." : "Salvar Empresa"}
            </button>
          </div>

        </form>
      </div>
    </Layout>
  );
}

export default NovaEmpresa;