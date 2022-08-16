# classs : pada daranya itu oop/pemograman berbasis objek . atau bisa diseut template atau blue print yang bisa digunakan pada intences
# fungsinya mirip dengan def tapi lebih kompleks
# class sederhada
print('class sederhana')
class bocil(): # class ini adlah blue print
    #pass # pass ini untuk membuat class kosong tanpa membuat error sintak
    nama = 'nama' # ini adalah atribut

Sasuke = bocil() # Sasuke adalah intences
Naruto = bocil() # Naruto juga intences
print(Sasuke.nama)
print(Naruto.nama)
print('-'*20)

# cara berubah nama bocil
Sasuke.nama = 'sasuke......!!!' # coba gunakan rumus : intences.atribut_pada_class
Naruto.nama = 'naruto.......!!!!'

print(Sasuke.nama)
print(Naruto.nama)

#class dengan method/fungsi
print('class dengan method/fungsi')

class bocah ():
    nama = 'nama'
    def barmaeng(self,keadaan):# keadaan ini bisa di isi apa saja terserah dan cara isinya tinggal lihat saja line 41
        print(self.nama,'sedang main Api gratis',keadaan)
    def makan (self): # self ini nempel dengan mothodnya
        print(self.nama,'sedang makan micin')


Sasuke = bocah()
Naruto = bocah()
Sasuke.nama = 'sasuke'
Naruto.nama = 'naruto'
print(Sasuke.nama)
print(Naruto.nama)
print('-'*20)

Sasuke.barmaeng('saat jaringan ngelag')
Naruto.makan()

