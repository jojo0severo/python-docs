## O que significa "if __name__ == "__main__"" em python?

Em python, quando você cria um arquivo .py, ele é considerado um módulo. Quando você executa um módulo python, o interpretador define a variável especial `__name__` para ter o valor `__main__`. Se você importar esse módulo em outro módulo, o `__name__` não será `__main__`.

Então, se você quiser executar algumas instruções apenas quando você executar o módulo como um programa principal, você pode fazer:
```python
    if __name__ == "__main__":
        # execute somente quando executado como um programa principal
        print("Executado como um programa principal")
    else:
        # execute somente quando importado como um módulo
        print("Executado como um módulo")
```

## O que significa um underscore antes de uma variável em python?

Um underscore antes de uma variável em python significa que a variável é protegida, ou seja, é desecorajado o uso dela fora da classe, mas não irá gerar um erro se você fizer. Por exemplo, se você quiser criar uma classe com uma variável protegida, você pode fazer:
```python
    class MyClass:
        def __init__(self):
            self._protected_var = 0
```


## O que significa dois underscores antes de uma variável em python?

Dois underscores antes de uma variável em python significa que a variável é privada e ela não pode ser acessada fora da classe ou gerará um erro. Por exemplo, se você quiser criar uma classe com uma variável privada, você pode fazer:
```python
    class MyClass:
        def __init__(self):
            self.__privateVar = 0
```

## O que significa um underscore antes e depois de uma variável em python?

Um underscore antes e depois de uma variável em python significa que a variável é temporária ou usada para evitar conflitos com palavras-chave. Por exemplo, se você quiser criar uma classe com uma variável temporária, você pode fazer:
```python
    class MyClass:
        def __init__(self):
            self.__temp__ = 0
```

## O que significa um underscore depois de uma variável em python?

Um underscore depois de uma variável em python significa que a variável não deve ser usada. Por exemplo, se você quiser criar uma classe com uma variável que não deve ser usada, você pode fazer:
```python
    class MyClass:
        def __init__(self):
            self._dontuse = 0
```

## O que significa um underscore antes e depois de uma função em python?

Um underscore antes e depois de uma função em python significa que a função é privada. Por exemplo, se você quiser criar uma classe com uma função privada, você pode fazer:
```python
    class MyClass:
        def __init__(self):
            self.__privateFunc()
        def __privateFunc(self):
            print("Executado como uma função privada")
```

## O que significa um underscore antes de uma função em python?

Um underscore antes de uma função em python significa que a função é usada internamente. Por exemplo, se você quiser criar uma classe com uma função usada internamente, você pode fazer:
```python
    class MyClass:
        def __init__(self):
            self._internalFunc()
        def _internalFunc(self):
            print("Executado como uma função usada internamente")
```