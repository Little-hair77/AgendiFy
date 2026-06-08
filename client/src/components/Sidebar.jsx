import { NavLink, useNavigate } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
  const navigate = useNavigate();

  // Função para deslogar do sistema
  const handleLogout = () => {
    // Apaga a chave de segurança do cofre do navegador
    localStorage.removeItem("@AgendiFy:token");
    navigate("/"); 
  };

  return (
    <div className="sidebar">
      <div className="sidebar-brand">
        AgendiFy
      </div>

      <nav className="sidebar-nav">
        <NavLink to="/dashboard" className="nav-item">
           Dashboard
        </NavLink>

        <NavLink to="/empresas" className="nav-item">
           Empresas
        </NavLink>

        <NavLink to="/profissionais" className="nav-item">
           Profissionais
        </NavLink>

        <NavLink to="/servicos" className="nav-item">
           Serviços
        </NavLink>
      </nav>

      <button className="logout-btn" onClick={handleLogout}>
        Sair do Sistema
      </button>
    </div>
  );
}

export default Sidebar;