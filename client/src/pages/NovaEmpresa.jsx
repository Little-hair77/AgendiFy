import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css"; 

function NovaEmpresa() {
  const navigate = useNavigate();
  
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const [endereco, setEndereco] = useState("");
  const [telefone, setTelefone] = useState("");
  const [email, setEmail] = useState("");
  
  const [salvando, setSalvando] = useState(false);

  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    try {
      await api.post("/empresas/", {
        nome: nome,
        descricao: descricao,
        endereco: endereco,
        telefone: telefone,
        email: email
      });

      alert("Empresa cadastrada com sucesso!");
      navigate("/empresas"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao cadastrar empresa. Verifique os dados e tente novamente.");
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
            <label>Nome da Empresa *</label>
            <input 
              type="text" 
              placeholder="Ex: The Wise Robótica Educacional"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>E-mail *</label>
            <input 
              type="email" 
              placeholder="contato@empresa.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Telefone *</label>
            <input 
              type="tel" 
              placeholder="(00) 00000-0000"
              value={telefone}
              onChange={(e) => setTelefone(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Endereço *</label>
            <input 
              type="text" 
              placeholder="Rua, Número, Bairro, Cidade"
              value={endereco}
              onChange={(e) => setEndereco(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Descrição</label>
            <textarea 
              placeholder="Uma breve descrição sobre a empresa..."
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