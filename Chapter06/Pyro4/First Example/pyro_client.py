import Pyro4

#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()

# Mendapatkan Nama
name = input("Siapa Nama Anda? ").strip()

# Mendapatkan Umur
umur = input("Berapa Umur Anda? ")
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.SelamatDatang(name))

print(server.menyapa(name))

print(server.sapa_full(umur, name))




