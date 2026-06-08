import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Layout from "../components/Layout";
import api from "../services/api";
import "./Formularios.css"; 

function FormularioEmpresa() {
  const navigate = useNavigate();
  const { id } = useParams(); // Pega o ID da URL, se existir
  const isEdicao = Boolean(id); // Se tem ID, estamos no modo Edição
  
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const [endereco, setEndereco] = useState("");
  const [telefone, setTelefone] = useState("");
  const [email, setEmail] = useState("");
  
  const [carregandoDados, setCarregandoDados] = useState(isEdicao);
  const [salvando, setSalvando] = useState(false);

  // Se for edição, busca os dados da empresa para preencher o formulário
  useEffect(() => {
    if (isEdicao) {
      buscarEmpresaParaEdicao();
    }
  }, [id]);

  const buscarEmpresaParaEdicao = async () => {
    try {
      const resposta = await api.get(`/empresas/${id}/`);
      const emp = resposta.data;
      setNome(emp.nome || "");
      setDescricao(emp.descricao || "");
      setEndereco(emp.endereco || "");
      setTelefone(emp.telefone || "");
      setEmail(emp.email || "");
    } catch (error) {
      console.error("Erro ao buscar empresa:", error);
      alert("Erro ao carregar os dados da empresa. Ela pode ter sido excluída.");
      navigate("/empresas");
    } finally {
      setCarregandoDados(false);
    }
  };

  const handleSalvar = async (e) => {
    e.preventDefault(); 
    setSalvando(true);

    const payload = { nome, descricao, endereco, telefone, email };

    try {
      if (isEdicao) {
        // Modo Edição: Manda um PUT para a URL específica da empresa
        await api.put(`/empresas/${id}/`, payload);
        alert("Empresa atualizada com sucesso!");
      } else {
        // Modo Criação: Manda um POST para a lista geral
        await api.post("/empresas/", payload);
        alert("Empresa cadastrada com sucesso!");
      }
      navigate("/empresas"); 
    } catch (error) {
      console.error("Erro ao salvar:", error);
      alert("Erro ao salvar os dados. Verifique as informações e tente novamente.");
    } finally {
      setSalvando(false);
    }
  };

  return (
    <Layout>
      <div className="page-header">
        {/* Título dinâmico baseado no modo atual */}
        <h1 className="page-title">{isEdicao ? "Editar Empresa" : "Nova Empresa"}</h1>
      </div>

      <div className="form-container">
        {carregandoDados ? (
          <div style={{ textAlign: "center", padding: "20px", color: "#64748b" }}>
            Carregando dados da empresa...
          </div>
        ) : (
          <form onSubmit={handleSalvar}>
            
            <div className="form-group">
              <label>Nome da Empresa *</label>
              <input 
                type="text" 
                placeholder="Ex: Barbearia The Wise"
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
                {/* Botão dinâmico */}
                {salvando ? "Salvando..." : isEdicao ? "Salvar Alterações" : "Cadastrar Empresa"}
              </button>
            </div>

          </form>
        )}
      </div>
    </Layout>
  );
}

export default FormularioEmpresa;