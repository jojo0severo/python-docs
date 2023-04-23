## fastapi

Provém uma forma simples e rápida de criar APIs RESTful com Python 3.6+ baseado no padrão de projeto OpenAPI e utilizando o framework web ASGI Starlette.

### Vantagens out-of-the-box

- Documentação automática da API: swagger é gerado utilizando anotações do código como docstrings, tipagem de parametros e tipagem de retorno
- Validação de dados: automaticamente valida os dados de entrada e de saída da API para forçar o formato informado
- Testes automatizados: fornece uma interface para testar a API através do testclient.TestClient

### Organização

- simple_app: somente o básico do uso do fastapi
- big_app: production ready api example


### Executar


Basta rodar os comandos: 
- `python -m big_app`
- `python -m simple_app`