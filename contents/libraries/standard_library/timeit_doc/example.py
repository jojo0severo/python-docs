import timeit


def example_timeit():
    print("\nExample timeit")
    print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
    print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
    print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
    print()

def example_repeat():
    print("\nExample repeat")
    print(timeit.repeat('"-".join(str(n) for n in range(100))', number=10000, repeat=3))
    print(timeit.repeat('"-".join([str(n) for n in range(100)])', number=10000, repeat=3))
    print(timeit.repeat('"-".join(map(str, range(100)))', number=10000, repeat=3))
    print()


example_timeit()
example_repeat()