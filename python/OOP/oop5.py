class Hero :

    def __init__(self,input_nama,nyawa,serangan,armor):
        #variabel intences
        self.nama = input_nama
        self.nyawa = nyawa
        self.serangan = serangan
        self.armor = armor

    def serang (self,lawan):
        print (self.nama + " menyerang " + lawan.nama) # terserah argumennya begimana yang penting argunemennya memiliki variabel nama itu sudah cukup
        pemukul.diserang(self,self.serangan) #self ini adalah heronnya dan juga ini akan memanggil fungsi diserang

    def diserang (self,lawan,serangan_lawan):
        print(self.nama + " terkena serangan dari "+lawan.nama)
        serangan_diterima= serangan_lawan/self.armor # ini adalah rumus untuk serangan yang diterima
        print("serangan yang diterima : " + str(serangan_diterima))
        self.nyawa -= serangan_diterima # ini adalah rumus untuk nyawa yang tersisa
        print('nyawa ' + self.nama + ' tersisa ' + str(self.nyawa))

penembak = Hero("Bambang si penembak handal",1000,50,10)
pemukul = Hero("Udin si tukang pukul",1100,45,10)



penembak.serang(pemukul) # ini akan memanggil fungsi serang
print("\n")
pemukul.serang(penembak) # ini di pemukul menyerang penembak cara kerjanya juga sama kayak di line 26
print("\n")
