import multiprocessing
from myFunc import myFunc
from random import randint, randrange

if __name__ == '__main__':
    for i in range(randint(6, 10)):
        list_names = ['Bobon', 'Toni', 'Tono', 'Budi', 'Sinta', 'Doni']

        number = randrange(len(list_names))
        nama = list_names[number]

        process = multiprocessing.Process(target=myFunc, args=(i, nama))
        process.start()
        process.join()

