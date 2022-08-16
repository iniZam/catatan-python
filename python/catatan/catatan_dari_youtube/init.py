class bocah ():

    def __init__(self,masukannama,masukannim) : # init adalah fungsi yang akan otomatis langsung berjalan saat class dipanggil
        self.nama = masukannama
        self.nim = masukannim

    def barmaeng(self,keadaan):# keadaan ini bisa di isi apa saja terserah dan cara isinya tinggal lihat saja line 41
        print(self.nama,'sedang main Api gratis',keadaan)

    def makan (self): # self ini nempel dengan mothodnya
        print(self.nama,'sedang makan micin')

Sasuke = bocah('sasuke uciha',1212) # ini sekaligus versi lebih sederhana dari script class line 25-42


print(Sasuke.nama) # ini dari line 4
print(Sasuke.nim) # ini dari line 5

Sasuke.barmaeng('semangat')