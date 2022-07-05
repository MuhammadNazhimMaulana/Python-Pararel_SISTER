import multiprocessing
import time
from random import randint, randrange

def myFunc():
    name = multiprocessing.current_process().name
    print ("Memulai Pemeriksaan = %s \n" %name)
    time.sleep(randint(2, 10))
    print ("Pemeriksaaan Selesai = %s \n" %name)

if __name__ == '__main__':
    processes = ['Pemeriksaan', 'Pembelian Obat', 'Pembayaran']

    i = randrange(len(processes))
    proses = processes[i]

    process_with_name = multiprocessing.Process\
                        (name=proses,\
                         target=myFunc)

    #process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process\
                                (target=myFunc)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
    
