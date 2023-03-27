# Note - we are using time.sleep to mimic i/o operations
import threading
import time

def func1_thread1():
    for i in range(10):
        time.sleep(2)
        print("active_count: "+  str(threading.active_count())) # actual user threads at this particular time
        print("native thead id: "+ str(threading.get_native_id())) # 
        print("first thread: "+ str(i))

def func2_thread2():
    for i in range(10):
        time.sleep(2)
        print("active_count: "+ str(threading.active_count())) # actual user threads at this particular time
        print("native thead id: "+ str(threading.get_native_id())) # 
        print("second thread: "+ str(i))
    
def main_func():
    start_time = time.time()
    thread1 = threading.Thread(target = func1_thread1)
    thread2 = threading.Thread(target = func2_thread2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()
    result = end_time - start_time
    print(result)

main_func() 