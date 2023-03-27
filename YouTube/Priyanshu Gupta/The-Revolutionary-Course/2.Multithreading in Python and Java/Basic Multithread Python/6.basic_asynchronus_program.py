import threading
from threading import Thread
import time
import multiprocessing
from multiprocessing import Process
import asyncio

async def async_help_func():
    loop = asyncio.get_running_loop()
    print(loop)
    for i in range(10):
        await asyncio.sleep(2)
        print(threading.active_count()) #actual user threads at this particular time
        print(str(threading.get_native_id()) + "first thread: "+ str(i))
    
async def mainfunc():
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    await asyncio.gather(async_help_func(), async_help_func())


    # loop.create_task(async_help_func())
    # loop.create_task(async_help_func())

    # same as asyncio.create_task()
    # asyncio.ensure_future(async_help_func())

    
    end_time = time.time()
    result = end_time - start_time
    print(result)

if __name__ == '__main__':
    asyncio.run(mainfunc())
