# Python Docs

Esse repositório serve como um guia para a documentação do Python.


Ele contém informações de bibliotecas muito utilizadas que são fornecidas junto com o interpretador, assim como algumas bibliotecas que são utilizadas, mas precisam ser instaladas por meio do PyPi.


Além de informações de bibliotecas, também é possível encontrar conteúdos sobre a linguagem python, como por exemplo, o que são módulos, pacotes, classes, funções, etc.

---

## Organização

A organização do repositório é feita da seguinte forma:
- contents: contém as documentações e exemplos
    - language: contém informações sobre a linguagem python separadas por pacotes
    - libraries: contém informações sobre bibliotecas separadas em dois blocos
        - standard-library: contém informações sobre as bibliotecas padrões do python da seguinte forma `<nome-da-biblioteca>_doc`
        - third-party-libraries: contém informações sobre bibliotecas de terceiros da seguinte forma `<nome-da-biblioteca>_doc`

- .gitignore: arquivo de configuração do git para ignorar arquivos e pastas gerado em `gitignore.io`

---

## O que é PyPi

PyPi é o acrônimo de Python Package Index, que é um repositório de pacotes Python.

---

## Como instalar um pacote

Para instalar um pacote, basta executar o seguinte comando:

```bash
pip install <nome-do-pacote>
```
