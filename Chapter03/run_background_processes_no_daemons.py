import multiprocessing
import time
from random import randint
from time import ctime

def foo(number):
    name = multiprocessing.current_process().name
    print ("Nomor Terpilih %s Mulai %s \n" %(number, name))
    if name == 'background_process':
        for i in range(0,5):
            print('%s ---> %d \n' % (ctime(), i))
        time.sleep(1)
    else:
        for i in range(5,10):
            print('%s ---> %d \n' % (ctime(), i))
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo, args=(randint(6, 10),))
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo, args=(randint(6, 10),))
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    

