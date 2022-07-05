import multiprocessing
from random import randrange
from time import ctime, sleep

class Processku(multiprocessing.Process):

    def run(self):
        print ('%s Memanggil method dalam %s' % (ctime(), self.name))
        sleep(randrange(5, 10))
        return

if __name__ == '__main__':
    for i in range(randrange(10, 15)):
        process = Processku()
        process.start()
        process.join()

