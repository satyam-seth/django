import time
from threading import Thread

def func1_thread1():
    for i in range(1000000):
        print("first thread: "+ str(i))

def func2_thread2():
    for i in range(1000000):
        print("second thread: "+ str(i))
    
def main_func():
    start_time = time.time()
    thread1 = Thread(target = func1_thread1)
    thread2 = Thread(target = func2_thread2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()
    result = end_time - start_time
    print(result)

main_func() 