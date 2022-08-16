class bocil ():

    sekolah = "masih SD soalnya dia bocil"
    __instalgame = 1 # ini adlah variabel privat yang hanya bisa diakses dan diubah dari dalam class saja
    # cara agar dia menjadi variabel privat adalah tinggal tambahkan 2 underscout saja(__)

    def __init__(self,masukannama,masukannim) : 
        self.nama = masukannama # ini adalah variabel publik yang bisa diakses dan diubah di luar class
        self.nim = masukannim # ini juga variabel publik

    def gameberat(self,tambahgame): # ini adalah salah satu cara untuk megubah dan mengakses variabel privat
        self.__instalgame += tambahgame

    def gameringan(self,tambahgame): # ini adalah salah satu cara untuk megubah dan mengakses variabel privat
        self.__instalgame += tambahgame

    def cekhp(self):
        if self.__instalgame <= 5:
            print (self.nama,' hp masih kuat')
        
        else :
            print(self.nama,' hp so tra mampo tu')

Sasuke = bocil('sasuke uciha',1212) 
Naruto = bocil('Naruto uzumaki',1213)

Sasuke.gameringan(4) # ini salah satu cara mengakses variabel privat dari dalam class
Sasuke.gameberat(1)

Sasuke.cekhp()