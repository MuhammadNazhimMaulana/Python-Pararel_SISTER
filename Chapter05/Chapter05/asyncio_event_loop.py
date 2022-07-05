import asyncio
import time
import random
from random import randrange

def tugas_web(waktu_selesai, pengulangan):
    print ("Tugas Web Dimulai")
    time.sleep(random.randint(0, 5))
    if (pengulangan.time() + 1.0) < waktu_selesai:
        pengulangan.call_later(1, tugas_program, waktu_selesai, pengulangan)
    else:
        pengulangan.stop()
        print ("Pengerjaan Tugas Telah Selesai")

def tugas_program(waktu_selesai, pengulangan):
    print ("Tugas Program Dimulai")
    time.sleep(random.randint(0, 5))
    if (pengulangan.time() + 1.0) < waktu_selesai:
        pengulangan.call_later(1, tugas_arsitektur, waktu_selesai, pengulangan)
    else:
        pengulangan.stop()
        print ("Pengerjaan Tugas Telah Selesai")

def tugas_arsitektur(waktu_selesai, pengulangan):
    print ("Tugas Arsitektur Dimulai")
    time.sleep(random.randint(0, 5))
    if (pengulangan.time() + 1.0) < waktu_selesai:
        pengulangan.call_later(1, tugas_bahasa, waktu_selesai, pengulangan)
    else:
        pengulangan.stop()
        print ("Pengerjaan Tugas Telah Selesai")


def tugas_bahasa(waktu_selesai, pengulangan):
    print ("Tugas Bahasa Dimulai")
    time.sleep(random.randint(0, 5))
    if (pengulangan.time() + 1.0) < waktu_selesai:
        pengulangan.call_later(1, tugas_arsitektur, waktu_selesai, pengulangan)
    else:
        pengulangan.stop()
        print ("Pengerjaan Tugas Telah Selesai")

def opening(waktu_selesai, pengulangan):
    print ("Opening")
    time.sleep(random.randint(0, 5))
    list_names = [tugas_arsitektur, tugas_bahasa, tugas_program, tugas_web]

    number = randrange(len(list_names))
    task = list_names[number]
    if (pengulangan.time() + 1.0) < waktu_selesai:
        print ("Mengerjakan Tugas Sesuai yang terpilih")
        pengulangan.call_later(1, task, waktu_selesai, pengulangan)
    else:
        pengulangan.stop()
        print ("Pengerjaan Tugas Telah Selesai")

pengulangan = asyncio.get_event_loop()
akhir_pengulangan = pengulangan.time() + random.randint(0, 60)
pengulangan.call_soon(opening, akhir_pengulangan, pengulangan)
pengulangan.run_forever()
pengulangan.close()

