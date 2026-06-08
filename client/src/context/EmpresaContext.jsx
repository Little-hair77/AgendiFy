import { createContext, useState } from "react";

export const EmpresaContext = createContext();

export function EmpresaProvider({ children }) {
  const [empresas, setEmpresas] = useState([
    { id: 1, nome: "Barbearia Premium", cnpj: "0001" },
    { id: 2, nome: "Salão Elegância", cnpj: "0002" },
  ]);

  function adicionarEmpresa(empresa) {
    setEmpresas((prev) => [
      ...prev,
      { ...empresa, id: Date.now() },
    ]);
  }

  function deletarEmpresa(id) {
    setEmpresas((prev) => prev.filter((e) => e.id !== id));
  }

  return (
    <EmpresaContext.Provider
      value={{
        empresas,
        adicionarEmpresa,
        deletarEmpresa,
      }}
    >
      {children}
    </EmpresaContext.Provider>
  );
}