# 🏥 Sistema de Agendamento de Serviços – Empresas Parceiras

Este projeto foi desenvolvido como parte da disciplina **Segurança em Sistemas de Informação** do **Instituto Federal Baiano**.  
O sistema permite o gerenciamento de **empresas parceiras**, **serviços**, **profissionais** e **agendamentos**, oferecendo um ambiente simples e seguro para controle de atendimentos.

---

## 🎯 Objetivo do Projeto

O objetivo deste sistema é:

- Facilitar o gerenciamento de **profissionais**, **empresas** e **serviços**;
- Permitir que administradores cadastrem e controlem todos os recursos;
- Oferecer aos usuários comuns apenas a função de visualização (sem edição);
- Demonstrar boas práticas de segurança e autorização no **Django**;
- Servir como base para aprendizado de desenvolvimento web seguro.

---

## 🚀 Projeto Django: Sistema de Gestão de Atividades

 - Este é um projeto de aplicação web desenvolvido em Django e Python, focado em demonstrar conceitos de desenvolvimento full-stack, segurança básica e padrões de design (FBVs).

## 🛠️ Ferramentas Necessárias

 - Para rodar este projeto em seu ambiente local, você precisará das seguintes ferramentas:

 - Python (Versão Recomendada 3.8+): Linguagem de programação principal.

 - pip (Gerenciador de Pacotes Python): Usado para instalar as dependências do Django.

 - Git: Para clonar o repositório e gerenciar versões.

 - Banco de Dados: SQLite (padrão do Django) ou outro SGBD configurado.

⚙️ Instruções de Execução

 - Siga os passos abaixo para colocar o projeto no ar:

1. Clonar o Repositório e Configurar o Ambiente

# 1. Clone o repositório
```bash
 git clone [(https://github.com/Little-hair77/Sistema-Agendamento-de-Servico)]
 cd [Sistema-Agendamento-de-Servico/Agendamento_de_Servico]
```
# 2. Crie e ative um ambiente virtual (RECOMENDADO)
```bash
 python -m venv venv
 source venv/Scripts/activate  # No Windows
 source venv/bin/activate    # No Linux/macOS
```
# 3. Instale as dependências (Django e outras bibliotecas)
```bash
 pip install -r requirements.txt
```

2. Configurar o Banco de Dados e Rodar Migrações

Você deve aplicar as migrações e, em seguida, popular o banco de dados com os usuários de teste.

# 4. Aplicar as migrações (cria as tabelas no BD)
```bash
 python manage.py migrate
 ```

# 5. Criar o superusuário (necessário para o ambiente Admin)
```bash
 python manage.py createsuperuser
```
# 6. (OPCIONAL) Carregar dados de teste
Se houver um arquivo de fixtures (initial_data.json)
```bash
 python manage.py loaddata initial_data.json
```

# 7. Iniciar o Servidor
```bash

 python manage.py runserver

```
Acesse a aplicação em seu navegador: http://127.0.0.1:8000/

## 🔑 Credenciais de Acesso (Para Teste)

 - Use estas contas para testar os diferentes níveis de acesso no sistema.

## ▶️ Instruções de Execução Super User

Esta conta tem acesso total ao Admin Django e a todas as funcionalidades.

SuperUser: admin@gmail.com

Senha: 1234

## ▶️ Instruções de Execução Usuários

Estas contas são para simular o acesso de usuários comuns e testar as permissões padrão.

Usuário 1: pablo.henrique@gmail.com

Usuário 2: higoalvesads@gmail.com

Usuário 3: jhonrels@gmail.com

Usuário 4: joaopedro@gmail.com

Usuário 5: viniclussilva@gmail.com

Senha (para todos os usuários): 1234 

### **1. Clone o repositório**
```bash
git clone <https://github.com/Little-hair77/Sistema-Agendamento-de-Servico>
cd <Sistema de Agendamento>
```
## ▶️ Link do Vídeo no Youtube
https://youtu.be/gxNI8q4tj4U
