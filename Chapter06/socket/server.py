# server .py
import socket
import time

# create a socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
host=socket.gethostname()
port=5555

# bind to the port
serversocket.bind((host,port))

# queue up to 5 requests
serversocket.listen(5)

# establish a connection
while True:	
    clientsocket,addr=serversocket.accept()
    print ("Terhubung dengan[addr],[port]%s"%str(addr))

    # Waktu sekarang
    currentTime=time.ctime(time.time())+"\r\n"

    # Menyapa
    sapa="Halo Kawan"+"\r\n"

    # Angka
    angka="Angka"+"\r\n"

    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.send(sapa.encode('ascii'))
    clientsocket.send(angka.encode('ascii'))
    clientsocket.close()
