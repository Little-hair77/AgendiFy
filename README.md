# AgendiFy - Sistema de Agendamento de Serviços

## 📌 Sobre o Projeto

O **AgendiFy** é um sistema web desenvolvido para o gerenciamento de empresas parceiras, profissionais e serviços, permitindo o controle de agendamentos de forma segura e eficiente.

O projeto foi desenvolvido como trabalho acadêmico para a disciplina de **Laboratório de Programação  Web II** do **Instituto Federal Baiano (IF Baiano)**, utilizando uma arquitetura desacoplada entre Backend e Frontend.

---

## 🎯 Objetivos do Projeto

Este sistema foi idealizado não apenas como um requisito acadêmico, mas como a simulação de um produto real. Os principais objetivos desde a sua concepção incluem:

* **Digitalizar a Gestão de Atendimentos:** Oferecer uma plataforma centralizada para que empresas parceiras administrem seus profissionais, catálogo de serviços e agendamentos de forma intuitiva.
* **Estabelecer Controle de Privilégios:** Criar fluxos de acesso distintos, garantindo que administradores gerenciem os recursos enquanto usuários comuns interagem apenas com as funções de agendamento.
* **Desacoplar a Arquitetura (Full-Stack):** Separar as responsabilidades do sistema, criando um Backend robusto e independente que alimenta uma aplicação Cliente dinâmica, simulando um ambiente real de produção.
* **Garantir a Segurança dos Dados:** Implementar uma API RESTful blindada com mecanismos de autenticação e autorização padrão de mercado (OAuth2), protegendo rotas sensíveis contra acessos indevidos.
* **Proporcionar uma Experiência Moderna:** Desenvolver uma interface de usuário responsiva, fluida e amigável no frontend, com feedback visual em tempo real.
* **Aplicar a Teoria na Prática:** Consolidar os conhecimentos de engenharia de software e servir como um laboratório real para demonstrar os conceitos de Segurança em Sistemas de Informação.
---

## 🏗️ Arquitetura do Sistema

O projeto evoluiu para uma arquitetura híbrida e desacoplada, demonstrando a versatilidade do ecossistema, dividido em duas frentes:

### 1. Aplicação Principal (Django Full-Stack & API RESTful)
O núcleo central do sistema. Além de possuir sua própria estrutura web completa nativa do Django (incluindo painel administrativo e gestão de banco de dados), ele atua como o motor de regras de negócio. Através do **Django Rest Framework (DRF)**, esta aplicação expõe os endpoints protegidos para o mundo externo, gerenciando a persistência de dados e a emissão de tokens de autenticação.

### 2. Cliente Externo (React API Client)
Uma aplicação frontend totalmente isolada, desenvolvida em React. Ela atua exclusivamente como um **cliente consumidor da API**, atendendo ao requisito de integração com tecnologias externas. Seu papel é realizar a autenticação via OAuth2, armazenar o token com segurança e renderizar uma interface moderna (Dashboard e Listagens) consumindo os dados do servidor Django de forma assíncrona.

```text
AgendiFy/
│
├── api/        → Backend Django REST Framework
│
└── client/     → Frontend React + Vite
```

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python 3.8+
* Django
* Django REST Framework
* Django OAuth Toolkit
* django-cors-headers
* SQLite

### Frontend

* React
* Vite
* React Router DOM
* Axios
* JavaScript

---

## 🔒 Segurança Implementada

O projeto utiliza o protocolo OAuth2 através do Django OAuth Toolkit para autenticação dos usuários.

Principais recursos de segurança:

* Autenticação via Bearer Token
* Controle de acesso baseado em permissões
* Proteção de endpoints da API
* Comunicação segura entre frontend e backend
* Controle de CORS

---

## ⚙️ Instalação e Execução

### 1. Clonar o Repositório

```bash
git clone https://github.com/Little-hair77/AgendiFy.git

cd AgendiFy
```

---

## 🚀 Executando o (Django Full-Stack & API RESTful)

Entre na pasta da API:

```bash
cd api
```

Crie o ambiente virtual:

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

A API estará disponível em:

```text
http://localhost:8000/
```

---

## 🔑 Configuração OAuth2

Acesse o painel administrativo:

```text
http://localhost:8000/admin/
```

Crie uma nova aplicação OAuth:

### Configurações

| Campo                    | Valor                         |
| ------------------------ | ----------------------------- |
| Client Type              | Confidential                  |
| Authorization Grant Type | Resource Owner Password-Based |
| Name                     | React Client                  |

Após salvar, copie:

* Client ID
* Client Secret

Essas informações serão utilizadas pelo frontend.

---

## 💻 Executando o Frontend

Abra um novo terminal:

```bash
cd client
```

Instale as dependências:

```bash
npm install
```

Crie um arquivo `.env`:

```env
VITE_CLIENT_ID=seu_client_id

VITE_CLIENT_SECRET=seu_client_secret
```

Inicie o servidor React:

```bash
npm run dev
```

A aplicação estará disponível em:

```text
http://localhost:5173/
```

---

## 📂 Funcionalidades do Cliente (React)

> **Nota de Arquitetura:** Este frontend foi desenvolvido especificamente como uma simulação (Proof of Concept) para demonstrar o consumo seguro da API por uma aplicação externa em outra linguagem, cumprindo o requisito técnico do trabalho. Por esse motivo, a interface React foca na integração das operações essenciais de apenas 3 models principais, enquanto o sistema Django completo gerencia o restante das regras de negócio nos bastidores.

###  Empresas
* Listar empresas
* Cadastrar nova empresa
* Excluir empresa

###  Profissionais
* Listar profissionais
* Cadastrar novo profissional
* Excluir profissional

###  Serviços
* Listar serviços
* Cadastrar novo serviço
* Excluir serviço
### Autenticação

* Login OAuth2
* Controle de permissões
* Logout seguro

---

## 👨‍💻 Autores

**Pablo Henrique**
**Higo Pereira Alves**

Instituto Federal Baiano (IF Baiano)

Curso: Análise e Desenvolvimento de Sistemas

Disciplina: Laboratório de Programação Web II

---

## ▶️ Vídeos de Demonstração

Como o desenvolvimento foi documentado desde as etapas iniciais do projeto, a apresentação do sistema foi dividida em dois vídeos. Isso demonstra a evolução real do trabalho e facilita a avaliação de todos os requisitos exigidos:

**1. Estrutura do Backend e API (Django)**
* 🔗 **Link:** [Assistir no YouTube](https://youtu.be/gxNI8q4tj4U)
* 📝 **Resumo:** Apresentação da arquitetura do servidor, criação dos models relacionados e configuração base do sistema.

**2. Consumo da API e Interface Cliente (React, DRF e DOT)**
* 🔗 **Link:** [link do novo vídeo]
* 📝 **Resumo:** Demonstração prática do ecossistema completo em funcionamento. Aborda o fluxo de login e geração de token via OAuth2 (DOT), a interface do Cliente (React), a execução do CRUD completo consumindo a API RESTful (DRF) e testes práticos de segurança provando a proteção das rotas contra acessos não autorizados.
