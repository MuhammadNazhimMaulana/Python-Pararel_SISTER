import time
from do_something import * # Melakukan import dari file do_something.py (Import semua yang ada di file tersebut)

# Implementasi dari penggunaan function do_something yang dimana akan membuat sebuah ilst integer dengan jumlah eksekusi 10 kali
if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    n_exec = 11
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
