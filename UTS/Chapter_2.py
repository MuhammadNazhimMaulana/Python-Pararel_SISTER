from random import randrange
import threading
from threading import Barrier, Thread
from time import ctime, sleep

barrier = Barrier(2)

print('\n ### Beginning of Testing ###')

pengulangan = 2

def wait_barrier(name, waktu_tidur):
    for i in range(pengulangan):
        print('%s Mulai Memasak pada waktu %s' % (name, ctime()))
        sleep(waktu_tidur)
        print('%s Menunggu di dapur %s' % (name, ctime()))
        barrier.wait()
        name = threading.currentThread().getName()
        list_makanan = ['Tengkleng', 'Bakmi', 'Bakso', 'Bubur']

        number = randrange(len(list_makanan))
        makanan = list_makanan[number]
        sleep(randrange(2, 5))
        print('%s Membuat %s at: %s \n' % (name, makanan,ctime()))
    print('%s sudah selesai memasak pada waktu %s' % (name, ctime()))

baru = Thread(name='First Chef', target=wait_barrier, args=["baru", 1], group=None, kwargs=None)
baru_lagi = Thread(name='Second Chef', target=wait_barrier, args=["baru_lagi", 10], group=None, kwargs=None)
baru.start()
baru_lagi.start()