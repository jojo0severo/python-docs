# Utilizado para rodar o fastapi, é uma biblioteca para uso
# em produção que lida com distribuição de carga das requisições e etc.
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get("/", response_class=JSONResponse)
async def root(r: Request) -> dict[str, str]:
    """
    Parâmetro "r" é injetado pelo fastapi.

    O parâmetro "response_class" define o tipo de resposta
    que será retornado, nesse caso um JSON.
    """
    print(r.headers)
    return {"message": "Hello World"}


@app.get("/items/{item_id}", response_class=PlainTextResponse)
async def read_item(item_id: int) -> dict[str, str]:
    """
    Parâmetro "item_id" é injetado pelo fastapi, ele busca
    na url o valor do parâmetro e o converte para o tipo
    definido no parâmetro "item_id".

    O parâmetro "response_class" define o tipo de resposta
    que será retornado, nesse caso um texto puro.
    """
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me() -> dict[str, str]:
    """
    A anotação "dict[str, str]" é usada para definir o tipo
    de retorno da função, nesse caso um dicionário com uma
    chave do tipo string e um valor do tipo string.

    Esse tipo é utilizado pelo fastapi para gerar a documentação
    da API.
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id):
    """
    Olha a documentação para ver o que aparece se não é anotado
    nenhum tipo nas variáveis ou retorno.
    """
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app)
