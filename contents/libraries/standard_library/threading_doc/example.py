import threading
import time


def worker(i):
    """thread worker function"""
    print('Worker: ', i)
    time.sleep(1)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

