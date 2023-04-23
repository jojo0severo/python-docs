"""
Esse arquivo nào tem nenhuma chamada ou print porque tudo aqui é utilizado
somente pelo linter da IDE que estiver utilizando para verificar os tipos
e não é executado.

Facilita a leitura do código e a compreensão dos tipos.
"""

from typing import Any, TypeVar, Dict, Iterator, List, Literal, Callable, Optional, Union, overload, Generic, final, Type, cast


def example_any():
    """
   Any é usado para indicar que o tipo de uma variável pode ser qualquer coisa.
    É o tipo mais genérico que existe, e é usado para indicar que o tipo de uma variável não é conhecido.
    """
    x: Any = 1
    x = "hello"
    x = [1, 2, 3]
    x = {"a": 1, "b": 2}
    x = {"a", "b"}
    x = (1, 2, 3)
    x = True
    x = None


def example_type_var():
    """
    TypeVar é usado para definir tipos genéricos
    T é um tipo genérico
    f é uma função que recebe um tipo T e retorna um tipo T
    """
    T = TypeVar("T")

    def f(x: T) -> T:
        return x
    
    a = f(1)
    b = f("")


def example_dict():
    """
    Dict é usado para definir tipos que são dicionários
    x é um dicionário de strings para inteiros
    """
    x: Dict[str, int] = {"a": 1, "b": 2}
    
def example_iterator():
    """
    Iterators é usado para definir tipos que são iteradores
    x é um iterador de inteiros
    """
    x: Iterator[int] = iter([1, 2, 3])

def example_list():
    """
    List é usado para definir tipos que são listas
    x é uma lista de inteiros
    """
    x: List[int] = [1, 2, 3]

def example_literal():
    """
    Literal é usado para definir tipos que são literais
    x é um int que pode ser 1, 2 ou 3
    """
    x: Literal[1, 2, 3] = 1
    x = 2
    x = 3

def example_callable():
    """
    Callable é usado para definir tipos que são chamáveis
    x é uma função que recebe dois argumentos, um int e uma string, e retorna um bool
    """
    x: Callable[[int, str], bool] = lambda x, y: x == 1

def example_optional():
    """
    Optional é usado para definir tipos que podem ser None
    x é um int ou None
    """
    x: Optional[int] = 1
    x = None

def example_union():
    """
    Union é usado para definir tipos que podem ser um de vários tipos
    x é um int ou uma string
    """
    x: Union[int, str] = 1
    x = "hello"

def example_overload():
    """
    overload é usado para definir sobrecarga de funções
    a é um int
    b é uma string
    """
    @overload
    def f(x: int) -> int:
        ...

    @overload
    def f(x: str) -> str:
        ...

    def f(x):
        return x

    a = f(1)
    b = f("hello")

def example_generic():
    """
    Generic é usado para definir tipos genéricos, que podem ser usados em outras classes
    T é um tipo genérico, que pode ser usado em outras classes
    C é uma classe genérica, que pode ser usada em outras classes
    a é uma instância de C, que recebe um int
    b é uma instância de C, que recebe uma string
    """
    T = TypeVar("T")

    class C(Generic[T]):
        def __init__(self, x: T) -> None:
            self.x = x

    a = C(1)
    b = C("hello")

def example_final():
    """
    Final é usado para definir classes que não podem ser herdadas
    C é uma classe final, que não pode ser herdada
    D é uma classe que herda de C, que não pode ser herdada
    """
    @final
    class C:
        ...

    # Erro
    # class D(C):
    #     ...

def example_type():
    """
    Type é usado para definir tipos de classes
    x é um tipo de int
    x é um tipo de str
    """
    x: Type[int] = int
    x = str

def example_cast():
    """
    Cast é usado para converter um tipo em outro
    x é um int
    y é um str, que recebe um int
    """
    x: int = 1
    y: str = cast(str, x)
