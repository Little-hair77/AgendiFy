import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/",
});

api.interceptors.request.use(async (config) => {
  const token = localStorage.getItem("@AgendiFy:token");
  
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const fazerLogin = async (username, password) => {
  const dadosLogin = new URLSearchParams();
  dadosLogin.append('grant_type', 'password');
  dadosLogin.append('username', username);
  dadosLogin.append('password', password);
  
  // ATENÇÃO: Retorno de chaves privadas
  dadosLogin.append('client_id', import.meta.env.VITE_CLIENT_ID);
  dadosLogin.append('client_secret', import.meta.env.VITE_CLIENT_SECRET);

  // A requisição bate na rota de token (igualzinho fizemos no Python)
  const resposta = await axios.post('http://localhost:8000/o/token/', dadosLogin, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  });

  return resposta.data; 
};

export default api;