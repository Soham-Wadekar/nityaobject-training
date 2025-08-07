from threading import Thread, Lock
import time

lock = Lock()
counter = 0


def increment(name):
    global counter
    for _ in range(100000):
        with lock:
            current = counter
            time.sleep(0.00001)
            counter = current + 1
            print(name, counter)


threads = [Thread(target=increment, args=(f"Thread-{_}",)) for _ in range(3)]
[t.start() for t in threads]
[t.join() for t in threads]

print("Counter (unsafe):", counter)
