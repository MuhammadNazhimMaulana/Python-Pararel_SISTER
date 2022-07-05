import threading
from random import randint, randrange

def my_func(thread_number, name):
    return print('{} called by thread N°{}'.format(name, thread_number))


def main():
    threads = []
    for i in range(randint(15, 20)):
        list_names = ['Bobon', 'Toni', 'Tono', 'Budi', 'Sinta', 'Doni']

        number = randrange(len(list_names))
        nama = list_names[number]

        t = threading.Thread(target=my_func, args=(i, nama))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
