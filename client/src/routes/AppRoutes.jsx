import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Empresas from "../pages/Empresas";
import Profissionais from "../pages/Profissionais";
import Servicos from "../pages/Servicos";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/empresas" element={<Empresas />} />
        <Route path="/profissionais" element={<Profissionais />} />
        <Route path="/servicos" element={<Servicos />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;