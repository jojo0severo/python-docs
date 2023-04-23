from multiprocessing import Process, Pool, cpu_count, Queue, Pipe, Lock, Manager, Semaphore


def semaphore_function(sem, i):
    sem.acquire()
    print('hello', i)
    sem.release()


def semaphore_example():    
    sem = Semaphore(0)
    p = Process(target=semaphore_function, args=(sem, 0))
    p.start()
    sem.release()
    p.join()

def pool_function(x):
    return x*x

def pool_example():
    with Pool(processes=4) as pool:
        print(pool.map(pool_function, [1, 2, 3]))


def cpu_count_example():
    print(cpu_count())


def queue_function(q):
    q.put([42, None, 'hello'])

def queue_example():
    q = Queue()
    p = Process(target=queue_function, args=(q,))
    p.start()
    print(q.get())
    p.join()

def pipe_function(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def pipe_example():
    parent_conn, child_conn = Pipe()
    p = Process(target=pipe_function, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()


def lock_function(l, i):
    l.acquire()
    print('hello world', i)
    l.release()

def lock_example():
    lock = Lock()

    for num in range(10):
        Process(target=lock_function, args=(lock, num)).start()



def manager_function(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(10)

def manager_example():
    with Manager() as manager:
        d = manager.dict()
        l = manager.list()

        p = Process(target=manager_function, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
    

if __name__ == '__main__':
    # Descomente cada um separadamente porque a execução em paralelo irá bagunçar 
    # os prints e não será possível saber qual é o resultado de cada um

    # manager_example()
    # lock_example()
    # pipe_example()
    # queue_example()
    # cpu_count_example()
    # pool_example()
    semaphore_example()