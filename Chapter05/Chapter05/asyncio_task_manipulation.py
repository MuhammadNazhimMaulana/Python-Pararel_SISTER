"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio
from asyncio import coroutine
from random import randint

coroutine
async def opening():
    print('Operasi Tugas Perhitungan dimulai')

coroutine
async def penjumlahan(number):
    fact = number + randint(0, 10)
    for i in range(2, number + randint(0, 5)):
        print('Tugas Penjumlahan: Perhitungan nomor (%s)' % i)
        await asyncio.sleep(randint(0, 5))
        fact += i
    print('Tugas - penjumlahan(%s) = %s' % (number, fact))


coroutine
async def pengurangan(number):
    fact = number - randint(0, 10)
    for i in range(number):
        print('Tugas Pengurangan: Pengurangan Nomor(%s)' % i)
        await asyncio.sleep(randint(0, 10))
        fact -= i
    print('Tugas - Pengurangan(%s) = %s' % (number, fact))


coroutine
async def perkalian(n, k):
    result = n * randint(0, 9)
    for i in range(1, k + 1):
        result = result*i
        print('Tugas Perkalian: Perhtiungan Perkalian Nomor (%s)' % i)
        await asyncio.sleep(randint(0, 9))
    print('Tugas - Perkalian(%s) = %s' % (n, result))


if __name__ == '__main__':
    list_tugas = [asyncio.Task(opening()),
                 asyncio.Task(penjumlahan(10)),
                 asyncio.Task(pengurangan(10)),
                 asyncio.Task(perkalian(20, 10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(list_tugas))
    loop.close()
