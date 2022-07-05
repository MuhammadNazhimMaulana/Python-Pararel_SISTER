import multiprocessing
import random
from random import randint
import time

class docter(multiprocessing.Process):
    def __init__(self, queue, jumlahAntrean):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.antre = jumlahAntrean

    def run(self) :
        for i in range(self.antre):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print ("Process Docter : nomor %d masuk antrean %s"\
                   % (item,self.name))
            time.sleep(1)
            print ("Jumlah Antrean %s"\
                   % self.queue.qsize())
       
class pacient(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Antrean Kosong")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Process Pasien : nomor %d dipegang \
                        oleh %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_docter = docter(queue, randint(15, 20))
        process_pacient = pacient(queue)
        process_docter.start()
        process_pacient.start()
        process_docter.join()
        process_pacient.join()
