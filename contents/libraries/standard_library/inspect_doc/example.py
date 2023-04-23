from inspect import getmembers, isfunction, isclass, ismethod, isbuiltin, ismethoddescriptor, isdatadescriptor, ismodule, isgeneratorfunction, isgenerator, isroutine, isabstract, ismethod, isfunction, isbuiltin, isgeneratorfunction, isgenerator, isroutine, isabstract, ismethod, isfunction, isbuiltin, isgeneratorfunction, isgenerator, isroutine, isabstract, ismethod, isfunction, isbuiltin, isgeneratorfunction, isgenerator, isroutine, isabstract, ismethod, isfunction, isbuiltin, isgeneratorfunction, isgenerator, isroutine, isabstract, ismethod, isfunction, isbuiltin, isgeneratorfunction, isgenerator


def example_getmembers():
    class A:
        def __init__(self) -> None:
            self.var1 = 10
            self.var2 = 20

    print("Getmembers:", getmembers(A))


def example_isfunction():
    def func():
        pass

    print("Is function:", isfunction(func))


def example_isclass():
    class A:
        pass

    print("Is class:", isclass(A))


def example_ismethod():
    class A:
        def method(self):
            pass

    print("is method:", ismethod(A.method))
    print("is method:", ismethod(A().method))


def example_isbuiltin():
    print("Is builtin:", isbuiltin(len))


def example_ismodule():
    import inspect

    print("Is module:", ismodule(inspect))


def example_isgeneratorfunction():
    def gen():
        yield 1

    print("Is generator function:", isgeneratorfunction(gen))


def example_isgenerator():
    def gen():
        yield 1

    print("Is generator:", isgenerator(gen()))

def example_isroutine():
    def func():
        pass

    class A:
        def method(self):
            pass

    print("Is routine:", isroutine(func))
    print("Is routine:", isroutine(A.method))

def example_isabstract():
    from abc import ABC, abstractmethod

    class A(ABC):
        @abstractmethod
        def method(self):
            raise NotImplementedError

    class B(A):
        pass

    class C(A):
        def method(self):
            return 10

    print("Is abstract:", isabstract(A))
    print("Is abstract:", isabstract(B))
    print("Is abstract:", isabstract(C))



example_getmembers()
example_isfunction()
example_isclass()
example_ismethod()
example_isbuiltin()
example_ismodule()
example_isgeneratorfunction()
example_isgenerator()
example_isroutine()
example_isabstract()
