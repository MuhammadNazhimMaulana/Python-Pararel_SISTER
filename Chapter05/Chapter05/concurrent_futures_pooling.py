import concurrent.futures
import time
from random import randint, randrange

number_list = list(range(1, randint(10, 115)))


def count(number):
    for i in range(0,randint(10, 100)):
        i += 1
    return i*number


def evaluate(item, name):
    result_item = count(item)
    print('Barang %s dengan nama pemilik %s, hasil %s' % (item, name, result_item))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.time()
    for item in number_list:
        list_nama = ['Bobon', 'Toni', 'Tono', 'Budi', 'Sinta', 'Doni']

        number = randrange(len(list_nama))
        name = list_nama[number]

        evaluate(item, name)
    print('Sequential Execution dalam %s seconds' % (time.time() - start_time))

   
    # Thread Pool Execution
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution dalam %s seconds' % (time.time() - start_time))

      
    # Process Pool Execution
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution dalam %s seconds' % (time.time() - start_time))
