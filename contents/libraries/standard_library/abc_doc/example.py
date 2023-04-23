from abc import ABC, abstractclassmethod, abstractmethod, abstractstaticmethod


class Animal(ABC):
    @abstractmethod
    def make_noise(self):
        raise NotImplementedError

    @abstractclassmethod
    def from_dict(cls, data):
        """
        Método que pode ser chamada no nivel da classe

        Exemplo: Animal.from_dict({"name": "Rex"})
        """
        raise NotImplementedError

    @abstractstaticmethod
    def get_type():
        """
        Método que pode ser chamado no nível da classe ou da instância

        Exemplo: Animal.get_animal_type()
        Exemplo: animal.get_animal_type()
        """
        raise NotImplementedError


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        return "Au au"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])

    @staticmethod
    def get_type():
        return "Dog"


class Cat(Animal):
    def __init__(self, name):
        self.name = name


dog1 = Dog("first")
dog2 = Dog.from_dict({"name": "second"})

print(dog1.get_type())
print(dog2.make_noise())


# Essa chamada gera erro porque a classe não implementou os métodos abstratos definidos
cat = Cat("error")
