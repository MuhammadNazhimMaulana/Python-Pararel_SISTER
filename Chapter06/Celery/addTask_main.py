###
#addTask.py : RUN the AddTask example with 
###

import addTask
from random import randint, randrange

if __name__ == '__main__':
    result = addTask.operasi(randint(10, 21), randint(1, 21))

    # Harapan Random
    list_harapan = ["Cuacanya Cerah", "Mendapatkan Uang yang Banyak", "Menjadi Presiden", "Beli Game Mahal"]

    nomor = randrange(len(list_harapan))
    harapan = list_harapan[nomor]
    result = addTask.harapan(harapan)
    
