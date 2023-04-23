from itertools import takewhile, starmap, accumulate, chain, repeat, product, permutations, pairwise, combinations, groupby, zip_longest, dropwhile, count


def example_takewhile():
    iterable = [1, 2, 3, 4, 5, 6]
    predicate = lambda x: x < 5
    result = takewhile(predicate, iterable)
    print("takewhile example:")
    print(list(result))
    print()


def example_starmap():
    iterable = [(1, 2), (3, 4), (5, 6)]
    function = lambda x, y: x * y
    result = starmap(function, iterable)
    print("starmap example:")
    print(list(result))
    print()


def example_accumulate():
    iterable = [1, 2, 3, 4, 5, 6]
    function = lambda x, y: x * y
    result = accumulate(iterable, function)
    print("accumulate example:")
    print(list(result))
    print()


def example_chain():
    iterable1 = [1, 2, 3, 4, 5, 6]
    iterable2 = [7, 8, 9, 10, 11, 12]
    result = chain(iterable1, iterable2)
    print("chain example:")
    print(list(result))
    print()


def example_repeat():
    iterable = [1, 2, 3, 4, 5, 6]
    result = repeat(iterable, 3)
    print("repeat example:")
    print(list(result))
    print()


def example_product():
    iterable1 = [1, 2, 3, 4, 5, 6]
    iterable2 = [7, 8, 9, 10, 11, 12]
    result = product(iterable1, iterable2)
    print("product example:")
    print(list(result))
    print()


def example_permutations():
    iterable = [1, 2, 3, 4, 5, 6]
    result = permutations(iterable, 3)
    print("permutations example:")
    print(list(result))
    print()


def example_pairwise():
    iterable = [1, 2, 3, 4, 5, 6]
    result = pairwise(iterable)
    print("pairwise example:")
    print(list(result))
    print()


def example_combinations():
    iterable = [1, 2, 3, 4, 5, 6]
    result = combinations(iterable, 3)
    print("combinations example:")
    print(list(result))
    print()


def example_groupby():
    iterable = [1, 2, 3, 4, 5, 6]
    function = lambda x: x % 2
    result = groupby(iterable, function)
    print("groupby example:")
    [print(f"({key}, {list(group)})", end=", ") for key, group in result]
    print("\n")


def example_zip_longest():
    iterable1 = [1, 2, 3, 4, 5, 6]
    iterable2 = [7, 8, 9, 10, 11, 12, 13, 14]
    result = zip_longest(iterable1, iterable2)
    print("zip_longest example:")
    print(list(result))
    print()


def example_dropwhile():
    iterable = [1, 2, 3, 4, 5, 6]
    predicate = lambda x: x < 5
    result = dropwhile(predicate, iterable)
    print("dropwhile example:")
    print(list(result))
    print()


def example_count():
    print("count example:")
    result = count(10, 2)
    for _ in range(5):
        print(next(result), end=", ")
    print()


example_takewhile()
example_starmap()
example_accumulate()
example_chain()
example_repeat()
example_product()
example_permutations()
example_pairwise()
example_combinations()
example_groupby()
example_zip_longest()
example_dropwhile()
example_count()