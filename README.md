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
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   Crie um arquivo `.env` com o comando:

   ```
   cp .env-example .env
   ```
   Crie uma SECRET_KEY executando:
   ```
   python utils/secret_gen.py
   ```
   Copie a secret_key e adicione na variável de ambiente SECRET_KEY no seu .env

5. Executando as migrações:

   ```
   python manage.py migrate
   ```

6. Rodando os testes:
   ```
   pytest
   ```

7. Crie um superusuário para ter acesso ao admin:
   ```
   python manage.py createsuperuser
   ```

8. Executando a aplicação:
   ```
   python manage.py runserver
   ```

Agora a API estará disponível em `http://localhost:8000`.

## Rotas

Link do insomnia com as requisições: 


OBS: 
- Autenticação é feita com o prefixo 'Token' seguido do authtoken criado após o login, que pode ser acessado pelo admin em Tokens.
- Apenas as requisições de cadastro de usuário e login não precisam de autenticação