import React, { useState } from "react";
import "./Login.css"; 
import { useNavigate } from "react-router-dom"; 
import { fazerLogin } from "../services/api"; 

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [erro, setErro] = useState("");
  
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault(); 
    setErro(""); 

    try {
      const resposta = await fazerLogin(username, password);

      localStorage.setItem("@AgendiFy:token", resposta.access_token);

      alert("Login realizado com sucesso!");
      
      navigate("/dashboard"); 

    } catch (error) {
      console.error("Erro no login:", error);
      setErro("Usuário ou senha incorretos. Tente novamente.");
    }
  };

  return (
    <div className="login-wrapper">
      <div className="login-card">
        
        <div className="login-header">
          <h2>Entrar no AgendiFy</h2>
          <p>Acesse sua conta para continuar</p>
        </div>
        
        {/* Mostra mensagem de erro se as credenciais estiverem erradas */}
        {erro && <div className="error-message">{erro}</div>}

        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label className="form-label">Usuário</label>
            <input 
              className="form-control"
              type="text" 
              value={username} 
              onChange={(e) => setUsername(e.target.value)} 
              placeholder="Digite seu usuário"
              required 
            />
          </div>

          <div className="input-group">
            <label className="form-label">Senha</label>
            <input 
              className="form-control"
              type="password" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              placeholder="Digite sua senha"
              required 
            />
          </div>

          <button type="submit" className="btn-login">
            Entrar
          </button>
        </form>

      </div>
    </div>
  );
};

export default Login;