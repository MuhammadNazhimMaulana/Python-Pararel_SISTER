import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, ctime
from datetime import datetime
from random import randint

def tes_dengan_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("%s process %s ----> %s" \
              %(ctime(), name,datetime.fromtimestamp(now)))

def tes_tanpa_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("%s process %s ----> %s" \
          %(ctime(), name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    total_barrier = randint(2, 10)
    synchronizer = Barrier(total_barrier)
    serializer = Lock()
    for i in range(total_barrier):
        Process(name='p'+str(i + 1)+' - tes_dengan_barrier'\
                ,target=tes_dengan_barrier,\
                args=(synchronizer,serializer)).start()

    Process(name='p3 - tes_tanpa_barrier'\
            ,target=tes_tanpa_barrier, args=[]).start()
    Process(name='p4 - tes_tanpa_barrier'\
            ,target=tes_tanpa_barrier, args=[]).start()
    


