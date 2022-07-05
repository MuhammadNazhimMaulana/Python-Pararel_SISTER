import asyncio
from asyncio import coroutine
import sys


coroutine
async def coroutine_pertama(future, num):
    count = 0
    for i in range(1, num):
        count -= 1
    await asyncio.sleep(4)
    future.set_result('Coroutine Pertama (Mengurangi n dengan 1) hasil akhirnya = %s' % count)


coroutine
async def courotine_kedua(future, num):
    count = 1
    for i in range(2, num):
        count *= i
    await asyncio.sleep(4)
    future.set_result('Coroutine Kedua (perkalian) hasilnya = %s' % count)

coroutine
async def courotine_ketiga(future, num):
    count = 1
    for i in range(2, 100):
        count += i * num
    await asyncio.sleep(4)
    future.set_result('Coroutine Ketigas Hasilnya = %s' % count)


def got_result(future):
    print(future.result())

if __name__ == '__main__':

    num = int(len(sys.argv[0]))

    loop = asyncio.get_event_loop()
    masaDepan1 = asyncio.Future()
    masaDepan2 = asyncio.Future()
    masaDepan3 = asyncio.Future()

    tasks = [coroutine_pertama(masaDepan1, num),
             courotine_kedua(masaDepan2, num),
             courotine_ketiga(masaDepan3, num)]

    masaDepan1.add_done_callback(got_result)
    masaDepan2.add_done_callback(got_result)
    masaDepan3.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
