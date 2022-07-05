import asyncio
from asyncio import coroutine
import time
from random import randint


coroutine
async def data_buku():
    print('DAFTAR BUKU\n')
    input_value = randint(0, 5)
    time.sleep(1)

    if input_value == 0:
        result = await tahap2(input_value)
    else:
        result = await tahap1(input_value)

    print('Daftar Buku : \n Total Buku ' + result)


coroutine
async def tahap1(transition_value):
    output_value = 'Jumlah buku = %s\n' % transition_value
    input_value = randint(0, 5)
    time.sleep(1)

    print('memuat data....')
    if input_value == 0:
        result = await tahap3(input_value)
    else:
        result = await tahap2(input_value)

    return output_value + 'tahap 1 meminjam, %s' % result


coroutine
async def tahap2(transition_value):
    output_value = 'Jumlah buku = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('memuat data....')
    if input_value == 0:
        result = await tahap1(input_value)
    else:
        result = await tahap3(input_value)

    return output_value + 'Tahap 2 mengembalikan, %s' % result


coroutine
async def tahap3(transition_value):
    output_value = 'Jumlah buku = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('memuat data....')
    if input_value == 0:
        result = await tahap1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + 'Tahap 3 membeli,  %s' % result


coroutine
async def end_state(transition_value):
    output_value = 'jumlah buku = %s\n' % transition_value
    print('selesai memuat data....')
    return output_value


if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(data_buku())