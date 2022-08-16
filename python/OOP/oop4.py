class hero :
    #variabel class
    jumlah_hero =0 

    def __init__(self,input_nama,inputnyawa,inputserangan,inputarmor):
        #variabel intences
        self.nama = input_nama
        self.nyawa = inputnyawa
        self.serangan = inputserangan
        self.armor = inputarmor
        hero.jumlah_hero += 1

    # ini adalah metod biasa saja tanpa argumen dan return
    def siapa(self) : # ini adalah salah satu method. dan metod adalah interaksi yang bisa dilakukan oleh objek
        print("halo aku adalah salah satu hero dan namaku adalah " + self.nama) # jadi saat metod ini dipanggil maka baris ini akan dieksekusi

    # ini metod dengan argumen tanpa return
    def tambahnyawa (self,tambah): # argumennya ada di dalam kurung ini yaitu tambah
        self.nyawa += tambah # jadi ini akan menambah nyawa hero sesuai dengan argumen tambah 

    # method dengan return tanpa agrumen
    def getnyawa(self):
        return self.nyawa

hero1 = hero("anak ajg",1200,120,200) 
hero2 = hero("udin",1200,500,120) 

hero1.siapa() # ini cara memanggil metodnya 

print(hero1.nyawa,'sebelum nyawa di tambah ')
hero1.tambahnyawa(100)
print(hero1.nyawa,"setelah nyawa ditambah")

print(hero1.getnyawa())