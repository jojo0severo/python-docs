import random


def example_seed():
    # "seed" define o início da geração de números
    # então toda execução com a mesma seed irá gerar a mesma
    # sequência de números

    print("Example seed:")
    random.seed(10)
    print(random.random())
    print(random.random())
    print(random.random())
    print()


def example_choice():
    print("Example choice:")
    print(random.choice('abcdefghij'))
    print()

def example_choices():
    print("Example choices:")
    print(random.choices([1, 2, 3, 4, 5, 6], k=4))  # choose 10 elements with replacement
    print()

def example_sample():
    print("Example sample:")
    print(random.sample([1, 2, 3, 4, 5, 6], k=3))  # choose 10 elements without replacement
    print()

def example_random():
    print("Example random:")
    print(random.random())  # random float
    print()

def example_randrange():
    print("Example randrange:")
    print(random.randrange(0, 101, 2))  # random even integer in range [0, 100]
    print()

def example_randint():
    print("Example randint:")
    print(random.randint(1, 10))  # random integer in range [a, b], including both end points
    print()


def example_shuffle():
    print("Example shuffle:")
    l = [1, 2, 3, 4, 5, 6]
    print("Before:", l)
    random.shuffle(l)   # shuffle list in place
    print("After:", l)
    print()

def example_distributions():
    print("Example distributions:")
    print(random.uniform(2.5, 10.0))
    print(random.expovariate(1 / 5))
    print(random.gammavariate(5, 1))
    print(random.gauss(0, 1))
    print(random.lognormvariate(0, 1))
    print(random.normalvariate(0, 1))
    print(random.vonmisesvariate(0, 1))
    print(random.paretovariate(1))
    print(random.weibullvariate(1, 1))
    print()


example_seed()
example_choice()
example_choices()
example_sample()
example_random()
example_randrange()
example_randint()
example_shuffle()
example_distributions()