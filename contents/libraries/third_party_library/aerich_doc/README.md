# aerich

Esse exemplo requer bibliotecas adicionais para executar:

-   pydantic: construção dos schemas
-   aiosqlite: conexão com banco de dados mysql
-   tortoise-orm: ORM para banco de dados

## Instalação

Para instalar as bibliotecas acima, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## Informações

O exemplo aqui utiliza o arquivo config.py para configurar os parâmetros de conexão com o banco de dados e gerar os schemas declarados na pasta "model".

Ele contém uma variável especial declarada nele que nomeamos de "TORTOISE_CONFIG" (poderia ser qualquer nome), ela será utilizada pelo aerich para carregar as configurações de conexão com o banco de dados.

## Setup

Antes de poder utilizar o aerich é necessário configurar o banco de dados com o tortoise, para isso execute o comando:

```bash
python config.py
```

Com o banco configurado podemos configurar o aerich agora, para isso rode os seguintes comandos:

```bash
aerich init -t config.TORTOISE_CONFIG
```

Esse comando irá criar uma pasta para as migrações do seu banco de dados e arquivos de configuração que o aerich irá usar internamente.

O parâmetro -t informa para o aerich onde ele irá encontrar a configuração do tortoise que será usada para encontrar os schemas e definir a conexão com o banco.

Depois disso, deve rodar o seguinte comando:

```bash
aerich init-db
```

Esse comando criará uma migração inicial que é o setup as-is do seu banco de dados como ele está no momento que esse comando foi executado, assim como declarar no banco sqlite essa migração.

## Execução

Com o aerich e o tortoise configurados propriamente, agora podemos utilizar comandos de migração do aerich. Esse exemplo, após o setup inicial, adicionou um novo campo na tabela Tournament chamado "cpf".

Mas considere que esse campo não faz mais sentido e você decidiu removê-lo, para isso basta:

1. Alterar o schema do tournamente removendo o campo
2. Executar o comando `aerich migrate --name remove-cpf-field` (ou qualquer outro nome que faça sentido).

O comando irá criar um novo registro no banco dessa migração e um novo arquivo na pasta de `migrations` contendo os comandos para atualizar o seu banco de dados. Porém o banco ainda não foi de fato alterado, para efetivar essa mudança basta rodar o comando:

```bash
aerich upgrade
```

Pronto, o banco foi alterado e a migração foi aplicada.

Caso deseja reverter a migração é possível com o comando:

```bash
aerich downgrade
```

Ou

```bash
aerich downgrade -v 1
```

Onde o argument -v é o numero no início do nome de cada uma das migrations, essa é a versão da mirgation.
Note que a versão informada é a que vai ser desfeita, não a versão que se deseja estar, ou seja, para voltar para a versão inicial do projeto é necessário aplicar downgrade de cada uma das versões subsequentes até a inicial.
