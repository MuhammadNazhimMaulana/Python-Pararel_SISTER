class namakelas:
    common = 10
    def __init__ (self):
        self.myvariable = 3
    def myfunction (self, arg1, arg2):
        return self.myvariable

instance = namakelas()
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))

instance2 = namakelas()
print("instance.common ",instance.common)
print("instance2.common ",instance2.common)

namakelas.common = 30

print("instance.common ", instance.common)

print("instance2.common ", instance2.common)

instance.common = 10
print("instance.common ", instance.common)

print("instance2.common " , instance2.common)
namakelas.common = 50

print("instance.common ", instance.common)
print("instance2.common " , instance2.common)

class AnotherClass (namakelas):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("hello")
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))

instance.test = 10
print("instance.test " , instance.test)

# Percobaan sendiri
print("\n ### Ini adalah hasil dari Class yang dibuat sendiri ### \n")

class Kucing:
    umur = 12
    def __init__(self):
        self.ekor = 1
        self.kaki = 4
    def bermain(self, majikan):
        activity = "Kucing memiliki " + str(self.ekor) + " buah ekor dan sedang bermain dengan"
        return activity + ' ' + majikan

# Mencoba memanggil function bermain
percobaan = Kucing()
print("percobaan.bermain(anto)" , percobaan.bermain("Anto"))

percobaanKedua = Kucing()
print("percobaanKedua.bermain(anto)" , percobaanKedua.bermain("Lala"))

# Memanggil umur
print("percobaanKedua.umur" , percobaanKedua.umur)
percobaanKedua.umur = 15

# Memanggil umur yang sudah di assgin dengan nilai baru
print("percobaanKedua.umur" , percobaanKedua.umur)

print("\n ### Membuat Class turunan dari Kucing ### \n")

# Membuat Class baru yang inherit dari class kucing
class AnakKucing (Kucing):
    def __init__(self, komen):
        self.ekor = 1
        print(komen)
    def belajar(self, teman):
        return teman

perocbaanKetiga = AnakKucing("Ini adalah komentar")

print("perocbaanKetiga.umur" , perocbaanKetiga.umur)

# Memanggil function dari class induk
print("perocbaanKetiga.bermain" , perocbaanKetiga.bermain("nino"))

# Function Buatan sendiri
print("perocbaanKetiga.belajar" , perocbaanKetiga.belajar("Mimin"))



