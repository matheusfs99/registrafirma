# Registra Firma

Registra Firma é uma API de cadastro de empresa com serviço de atualização de dados após verificação na api da Receita Federal a cada 30 dias após do cadastro da empresa.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- Celery
- Redis
- Docker
- SQlite

## Como usar

1. Clone o repositório:

   ```
   git clone https://github.com/matheusfs99/registrafirma.git
   ```

2. Inicie um ambiente virtual:
   ```
   cd registrafirma
   python3.11 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```
   make install
   ```

4. Configure as variáveis de ambiente:

   Crie um arquivo `.env` com o comando:

   ```
   cp .env-example .env
   ```
   Crie uma SECRET_KEY executando:
   ```
   make secret
   ```
   Copie a secret_key e adicione na variável de ambiente SECRET_KEY no seu .env

5. Executando a aplicação com docker-compose e build do projeto:

   ```
   make build
   ```

6. Rodando os testes:
   ```
   make test
   ```

7. Crie um superusuário para ter acesso ao admin:
   ```
   make createsuperuser
   ```

Agora a API estará disponível em `http://localhost:8000`.

## Rotas

Link do insomnia com as requisições: 

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Registra%20Firma&uri=https%3A%2F%2Fgithub.com%2Fmatheusfs99%2Fregistrafirma%2Fblob%2Fmaster%2Futils%2FRegistra_Firma_Insomnia.json)


OBS: 
- Autenticação é feita com o prefixo 'Token' seguido do authtoken criado após o login, que pode ser acessado pelo admin em Tokens.
- Apenas as requisições de cadastro de usuário e login não precisam de autenticação