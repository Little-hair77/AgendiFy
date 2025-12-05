🏥 Sistema de Agendamento de Serviços – Controle de Profissionais e Empresas
Projeto da disciplina Segurança em Sistemas de Informação — IF Baiano
📌 Objetivo do Sistema

O objetivo deste projeto é desenvolver um sistema seguro de controle de empresas, serviços e profissionais, com foco em:

Cadastro e gestão de empresas parceiras

Cadastro e gestão de serviços oferecidos

Gerenciamento de profissionais vinculados

Controle de acesso (Admin e Usuários comuns)

Boas práticas de segurança no backend (Django)

O sistema foi desenvolvido como atividade prática da disciplina Segurança em Sistemas de Informação, aplicando conceitos fundamentais de autenticação, autorização e gestão segura de dados.

👥 Integrantes do Grupo

Pablo Henrique Azevedo Gomes da Silva

Higo Pereira Alves

▶️ Vídeo de Apresentação

🔗 Insira aqui o link do vídeo após gravarem.
Exemplo:
https://youtu.be/seu-video

⚙️ Instruções de Execução
📁 1. Clone o repositório
git clone https://github.com/seu-repositorio/projeto-agendamento.git
cd projeto-agendamento

🐍 2. Crie e ative o ambiente virtual
python -m venv venv


Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

📦 3. Instale as dependências
pip install -r requirements.txt

🗂️ 4. Execute as migrações
python manage.py makemigrations
python manage.py migrate

👑 5. Acesse com o superusuário padrão

O sistema possui um superuser já definido para testes:

Usuário: admin@gmail.com
Senha: 1234


Caso precise criar outro administrador:

python manage.py createsuperuser

▶️ 6. Inicie o servidor
python manage.py runserver

🌐 7. Acesse no navegador
http://127.0.0.1:8000/

🔐 Papel dos Usuários
🟣 Administrador (Superuser)

Cadastra empresas

Cadastra serviços

Cadastra profissionais

Edita e remove qualquer registro

Gerencia usuários

🔵 Usuário Comum

Visualiza empresas parceiras

Visualiza serviços disponíveis

Visualiza profissionais

Não pode editar nem remover registros

🛡️ Principais Medidas de Segurança Implementadas

Autenticação por sessão com Django Auth

Permissões e restrição de acessos por nível de usuário

Templates protegidos (esconder botões de ação para usuários comuns)

Sanitização e validação de formulários

Regras de negócio controladas pela view e não pelo frontend

📄 Licença

Projeto acadêmico — uso livre para fins educacionais.