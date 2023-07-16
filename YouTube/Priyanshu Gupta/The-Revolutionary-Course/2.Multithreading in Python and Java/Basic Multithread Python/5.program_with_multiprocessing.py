import multiprocessing

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)\


def multiprocess_func():
    print("Number of cpu : ", multiprocessing.cpu_count())
    # names = ['America','Europe', 'Africa']
    names = range(100)
    procs = []
    proc = multiprocessing.Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = multiprocessing.Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    print("done")

if __name__ == '__main__':
    multiprocess_func()

