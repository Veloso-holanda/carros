# Projeto Carros 🚗

Loja de Carros – Aplicação Web desenvolvida com Python e Django. Projetada para simular uma loja de veículos com funcionalidades de autenticação e administração.

## Funcionalidades

- **Autenticação de Usuários**: sistema completo de login e registro, permitindo acesso seguro e gerenciamento de contas.
- **Gerenciamento de Veículos**: cadastro, edição, visualização e remoção de veículos, com atributos como modelo, marca, ano e preço.
- **Painel Administrativo**: espaço dedicado para administradores gerenciarem usuários e veículos de forma eficiente.
- **Interface Responsiva**: adaptação visual para diferentes tamanhos de tela, garantindo boa experiência em dispositivos diversos.

## Tecnologias Utilizadas

- **Backend**: Python, Django  
- **Frontend**: HTML, CSS  
- **Banco de Dados**: SQLite (possibilidade de migração para PostgreSQL)  
- **Controle de Versão**: Git, GitHub

## Objetivo do Projeto

Este projeto foi desenvolvido com o propósito de aplicar e aprimorar conhecimentos em desenvolvimento web com Django, focando em criação de aplicações robustas e escaláveis.

## Estrutura do Projeto

```
/
├── accounts/             # App para autenticação e gerenciamento de usuários
├── app/                  # App principal (a definir conforme context)
├── cars/                 # App relacionado à lógica de gerenciamento de veículos
├── manage.py             # Script de comando principal do Django
├── requirements.txt      # Dependências do projeto
├── carros_uwsgi.ini      # Configuração do uWSGI para deploy
├── uwsgi_params          # Parâmetros adicionais do uWSGI
├── .env                  # Arquivo de variáveis de ambiente (não versionado)
├── .gitignore            # Configura arquivos e pastas a serem ignorados pelo Git
└── README.md             # Arquivo atual (documentação)
```

## Requisitos

- Python 3.x  
- Pip (gerenciador de pacotes)
- (Opcional) Banco de dados PostgreSQL, se desejar substituir o SQLite

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Veloso-holanda/carros.git
   cd carros
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure variáveis de ambiente:
   - Copie o `.env.example` (se existir) para `.env`, ou crie um `.env` com chaves como `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.

5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário (opcional, para acesso administrativo):
   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

8. Acesse no navegador: `http://127.0.0.1:8000/`

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório.
2. Crie uma branch com sua feature ou correção:
   ```bash
   git checkout -b feat/nova-feature
   ```
3. Faça suas alterações e commite com clareza:
   ```bash
   git commit -m "Adiciona recurso X"
   ```
4. Faça push para sua branch:
   ```bash
   git push origin feat/nova-feature
   ```
5. Abra um Pull Request e aguarde revisão.

## Contato

Desenvolvido por [Gabriel Veloso de Souza] (Veloso‑holanda).  
Para sugestões, feedback ou dúvidas, você pode abrir uma issue ou enviar uma mensagem via GitHub.

