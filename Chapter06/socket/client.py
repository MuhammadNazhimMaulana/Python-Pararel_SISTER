# client .py
import socket
from random import randint

# create a socket object
s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
host=socket.gethostname()
port=5555

# connection to hostname on the port .
s.connect((host,port))

# Receive no more than 1024 bytes
tm=s.recv(1024)

hai=s.recv(1024)

angka=s.recv(1024)

s.close()

# Print Waktu 
print ("Waktu Koneksinya terhadap server:%s"%tm.decode('ascii'))

# Print Sapaan 
print(hai.decode('ascii'))

# Print Angka 
nomor = len(angka.decode('ascii'))
pembanding = randint(0, 11)

if(nomor > pembanding):
    print("Angka %s Lebih Besar Dari %s" % (nomor, pembanding))
else:
    print("Angka %s Lebih Kecil Dari %s" % (nomor, pembanding))
