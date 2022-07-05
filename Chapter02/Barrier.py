from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

barrier = Barrier(2)
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()

print('\n ### Beginning of Testing ###')

pengulangan = 2

def menunggu_barrier(name, waktu_tidur):
    for i in range(pengulangan):
        print('%s Bergerak pada waktu %s' % (name, ctime()))
        sleep(waktu_tidur)
        print('%s Menunggu di barrier %s' % (name, ctime()))
        barrier.wait()
    print('%s sudah selesai pada waktu %s' % (name, ctime()))

baru = Thread(target=menunggu_barrier, args=["baru", 1])
baru_lagi = Thread(target=menunggu_barrier, args=["baru_lagi", 10])
baru.start()
baru_lagi.start()