🧩 Sistema MVC com Flask e SQLite
📘 Descrição do Projeto

Este projeto foi desenvolvido como parte das atividades da disciplina de Análise e Desenvolvimento de Sistemas (4° semestre), com o objetivo de demonstrar o funcionamento do padrão de arquitetura MVC (Model-View-Controller) aplicado em uma aplicação web simples.

A aplicação permite o cadastro e listagem de produtos utilizando Flask como framework web e SQLite como banco de dados.
O sistema foi construído com foco na separação de responsabilidades, organização do código e aplicação prática dos conceitos de camadas de software.

🧠 Conceito Utilizado — MVC

O projeto segue a arquitetura MVC, onde:

Model (models.py) → Representa a camada de dados e regras de negócio.
Utiliza SQLAlchemy ORM para criar e manipular o banco SQLite (database.db).

View (templates/produtos.html) → Camada de interface responsável por exibir os dados ao usuário.
É construída com HTML e renderizada pelo Flask.

Controller (app.py) → Camada de controle que faz a ponte entre Model e View.
Gerencia as rotas da aplicação, as requisições HTTP e retorna as respostas adequadas.

⚙️ Tecnologias Utilizadas

Python 3

Flask – framework web minimalista

SQLAlchemy – ORM para interação com o banco de dados

SQLite – banco de dados leve e embutido

HTML / Jinja2 – motor de templates do Flask

🚀 Como Executar o Projeto

Criar ambiente virtual

python -m venv venv
venv\Scripts\activate     # (Windows)
# ou
source venv/bin/activate  # (Linux/Mac)


Instalar dependências

pip install flask sqlalchemy


Executar o servidor

python app.py


Acessar no navegador

http://127.0.0.1:5000/

🔍 Endpoints Disponíveis
Método	Rota	Descrição
GET	/	Exibe a página com a lista de produtos
GET	/api/produtos	Retorna todos os produtos em formato JSON
POST	/api/produtos	Adiciona um novo produto via JSON
Exemplo de POST (JSON)
{
  "nome": "Mouse Gamer",
  "preco": 150.0
}

🧮 Estrutura do Projeto
meu_app/
│
├── app.py              # Controller - gerencia rotas e requisições
├── models.py           # Model - define e manipula o banco de dados
├── database.db         # Banco SQLite gerado automaticamente
└── templates/
    └── produtos.html   # View - interface HTML para exibir os produtos

🎓 Objetivo Educacional

Este projeto tem como finalidade:

Demonstrar o uso do padrão MVC em aplicações web;

Aplicar conceitos de arquitetura de software e organização de camadas;

Integrar o uso de banco de dados relacional (SQLite) com aplicações Python;

Desenvolver habilidades práticas em Flask e SQLAlchemy;

Proporcionar uma base sólida para projetos maiores utilizando frameworks MVC.

✍️ Autor

Bruno Eduardo Luy
Estudante de Análise e Desenvolvimento de Sistemas – 4° Semestre
UDESC - Universidade Estadual de Santa Catarina
📅 Ano: 2025
