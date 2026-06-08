import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Empresas from "./pages/Empresas";
import Profissionais from "./pages/Profissionais";
import Servicos from "./pages/Servicos";
import FormularioEmpresa from "./pages/FormEmpresa";
import FormularioProfissional from "./pages/FormProfissional";
import FormServico from "./pages/FormServico"
import FormularioServico from "./pages/FormServico";

function App() {
  return (
    <BrowserRouter>
      {/* Removemos aquele <EmpresaProvider> que envelopava tudo aqui */}
      <Routes>
        {/* Rota Pública */}
        <Route path="/" element={<Login />} />

        {/* Rotas Privadas (Painel) */}
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/empresas" element={<Empresas />} />
        <Route path="/profissionais" element={<Profissionais />} />
        <Route path="/servicos" element={<Servicos />} />
        <Route path="/empresas/cadastrar" element={<FormularioEmpresa/>}/>
        <Route path="/empresas/editar/:id" element={<FormularioEmpresa/>}/>
        <Route path="/profissionais/cadastrar" element={<FormularioProfissional/>}/>
        <Route path="/profissionais/editar/:id" element={<FormularioProfissional/>}/>
        <Route path="/servicos/cadastrar" element={<FormularioServico/>}/>
        <Route path="/servicos/editar/:id" element={<FormularioServico/>}/>

        {/* Rotas de Criação (Desativadas até construirmos as telas) */}
        {/* <Route path="/empresas/nova" element={<NovaEmpresa />} /> */}
        {/* <Route path="/profissionais/novo" element={<NovoProfissional />} /> */}
        {/* <Route path="/servicos/novo" element={<NovoServico />} /> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;