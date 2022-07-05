#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing
from random import randrange
from time import ctime

def myFunc(i, orang):
    print ('Memanggil myFunc dari proses n°: %s dan yang dipilih adalah %s' % (i, orang))
    for j in range (0,i):
        print(' %s Keluaran dari myFunc adalah :%s' % (ctime(), j))
    return

if __name__ == '__main__':
    for i in range(6):
        list_names = ['Anto', 'Toni', 'Tono', 'Budi', 'Sinta']

        number = randrange(len(list_names))
        nama = list_names[number]

        process = multiprocessing.Process(target=myFunc, args=(i, nama))
        process.start()
        process.join()

