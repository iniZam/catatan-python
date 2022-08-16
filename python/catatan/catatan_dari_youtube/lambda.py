apa = lambda pam: print(pam)


def tambah (angka1,angka2): #ini pernjelasan lengkapnya ada di modul def
	hasil = angka1+angka2  
	return hasil

jumlah = lambda n,z : n+z #lambda adalah versi lebih simpel dari def di line 4. jadi pada dasarnya ini adalah fungsi
# rumus lambda : "varaiabel(ini anggap saja nama fungsinya) = lambda argumen : statement(ini seperti def bagian dibawahnya)" . biar jelas coba lihat di modul def line 71-74

jeng = jumlah(5,5) #fungsinya bisa dimasukan ke dalam variabel juga biar mudah dipanggil

apa('asu\tini fungsi dari line 1')
print (tambah(5,6),'\tini fungsi dari line 4-6') 
print(jumlah(2,2),'\t ini fungsi dari line 8') 
print(jeng,'\tini dari variabel di line 11') #\t ini fungsinya mirip seperti tombol tab(yg ada di atas shift tu)