import heapq


def heapsort(iterable):
    """
    Ordena a lista 'iterable' utilizando o heapq como uma pilha.
    Como todos os valores adicionados e retirados são ordenados pelo algoritmo interno do heapq
    cada pop no heapq será do menor elemento da lista.
    """
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


def compare_heap_with_list(iterable):
    """
    Compara o tempo de acesso dos menores elementos da lista
    """
    def set_heap():
        for value in iterable:
            heapq.heappush(h, value)
   

    import time
    import copy

    mean = 0
    total_executions = 1000

    h = []
    set_heap()
    
    for _ in range(total_executions):
        start = time.time()
        heapq.heappop(h)
        end = time.time()

        mean += end - start

        set_heap()

    print(f"heap: {mean/ total_executions}")

    mean = 0
    smallest = min(iterable)

    iterable_copy = copy.deepcopy(iterable)
    for _ in range(total_executions):
        start = time.time()
        iterable_copy.pop(iterable_copy.index(smallest))
        end = time.time()

        mean += end - start
        iterable_copy = copy.deepcopy(iterable)
 
    print(f"list: {mean/ total_executions}")


if __name__ == '__main__':
    print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

    import random
    big_list = list(range(1000))
    random.shuffle(big_list)
    compare_heap_with_list(big_list)