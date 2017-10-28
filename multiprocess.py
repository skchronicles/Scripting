##############################
# Skyler Kuhn
# Python's GIL Loophole
# Multiprocessing
##############################
from multiprocessing import Process, Manager


def proc(procNum):
    print('Proc' + str(procNum) + ': starting')
    result_list = [i**2 for i in range(10000000)]
    print('Proc' + str(procNum), result_list)
    print('Proc' + str(procNum) + ': finishing')


def runParallel(*fns):
        proc = []
        for fn in fns:
            p = Process(target=fn)
            p.start()
            proc.append(p)
        for p in proc:
            p.join()


def runMultipleOccureneces():
    processes_list = []
    for i in range(10):
        p = Process(target=proc, args=(i,))
        p.start()
        processes_list.append(p)
    for p in processes_list:
        p.join()


def main():
    #runParallel(proc1, proc2)
    runMultipleOccureneces()

if __name__ == '__main__':
    main()
