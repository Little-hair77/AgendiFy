import requests

URL_TOKEN = 'http://localhost:8000/o/token/'
URL_API = 'http://localhost:8000/api/profissionais/'

dados_login = {
    'grant_type': 'password',
    'username': 'nome_do_usuario_aqui',
    'password': 'senha_do_usuario_aqui',
    'client_id': 'seu_client_id_gerado_no_painel',
    'client_secret': 'seu_client_secret_gerado_no_painel'
}

print("1. Tentando fazer login...")

resposta_login = requests.post(URL_TOKEN, data=dados_login)

if resposta_login.status_code == 200:
    token = resposta_login.json()['access_token']
    print(f"✅ Login com sucesso! Token gerado: {token[:15]}...\n")
    
    print("2. Tentando acessar a rota protegida com o token...")
    headers = {'Authorization': f'Bearer {token}'}
    resposta_api = requests.get(URL_API, headers=headers)
    
    print("Resultado da API:")
    print(resposta_api.json())
else:
    print(f"❌ Falha no login. Erro: {resposta_login.text}")