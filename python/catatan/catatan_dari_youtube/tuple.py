#tuple = sama saja dengan list tapi tuple ini pake kurung biasa
angka = [1,2,3,4,5]
print(type (angka),angka)#type ini gunanya unruk menujukan tipe datanya

huruf = ('a','b','c','d','e','f','a',1,2,3,4,5,6) # ini tuple
print(type (huruf),huruf)#type ini gunanya unruk menujukan tipe datanya
#jadi bedanya tuple dengan list adalah data tuple tidak bisa diubah/dimanupulasi dan nilainya hanya bisa diakses dengan indeks dan count

angka [2]=10000 # ini masih bisa dirubah karena data angka adalah list
angka.append(100)
angka.append('asu')
print('data sekarang',angka,'\tini adalah variabel angka')
angka.remove('asu')# remove ini akan menghapus data yang dipilih di list(cara memilih datanya tinggal isi daja dalam kurungnya)
print('data sekarang',angka,'\tini adalah variabel angka')
#huruf [1]='bangsat kau'# ini tak bisa diubah karena data huruf adalah tipe tuple catatan : kalau mau line 15-18 di-run tinggal hapus saja tanda # di depan
#huruf.append('z')# ini tak bisa diubah karena data huruf adalah tipe tuple
#huruf.remove(2)# ini tak bisa diubah karena data huruf adalah tipe tuple
print(huruf)# jadi nilai tuple itu sudah valid dan tak bisa diubah

#print(dir(angka))# dir ini untuk mengetahui apa saja yang bisa digunakan dengan tipe data ini catatan : kalau mau line 20-21 di-run tinggal hapus saja tanda # di depan
#print(dir(huruf))# dir ini untuk mengetahui apa saja yang bisa digunakan dengan tipe data ini

print(huruf.index(1),'ini index') # indeks ini gunanya untuk mencari tau ada di line berapa data yang dipilih
print(huruf.count('a'),'ini count') # count ini gunanya untuk melihat ada jumlah data yang dipilih(cara memilih datanya tinggal isi daja dalam kurungnya)
