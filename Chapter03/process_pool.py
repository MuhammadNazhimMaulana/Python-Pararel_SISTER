#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
from random import randrange

def count_price(data):
    result = data*data
    return 'Rp.' + str(result)


if __name__ == '__main__':
    inputs = list(range(100,200))
    pool = multiprocessing.Pool(processes=randrange(1, 2))
    pool_outputs = pool.map(count_price, inputs)

    pool.close() 
    pool.join()  
    print ('List Harga   :', pool_outputs)
