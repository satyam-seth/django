# Note - we are using time.sleep to mimic i/o operations
import time

def func1_thread1():
    for i in range(10):
        time.sleep(2)
        print("first thread: "+ str(i))

def func2_thread2():
    for i in range(10):
        time.sleep(2)
        print("second thread: "+ str(i))
    
def main_func():
    start_time = time.time()
    func1_thread1()
    func2_thread2()
    end_time = time.time()
    result = end_time - start_time
    print(result)

main_func() 