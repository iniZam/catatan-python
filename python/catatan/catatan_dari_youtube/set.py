# set = himpunan. mirip seperti list dan tuple tapi ada bedanya
#cara buat himpunan ada 2 cara:
#cara 1:
print("hasil dari cara 1:")
himpunan_kucing = {"oren",
                   "tompel",
                   "hitam"}

himpunan_kucing.add("putih")
himpunan_kucing.add("buta")
himpunan_kucing.add("oren")#ini nanti saat di print data "oren" tidak akan nambah (penjelasaanya di line 12)
print("jenis-jenis kocheng: ",himpunan_kucing)
#nanti hasil printnya tidak berurutan. karena tipe data set(himpunan) itu tidak memedulikan urutan karena tipe data set itu hanya menampilkan data yang ada saja
#selain tidak memperhatikan urutan tipe data set juga tidak memperhatikan jumlahnya jadi mau ditambahkan sebanyak apapun jika datanya sama maka yang di print hanya 1

#cara 2
print("hasil dari cara 2:")
jenis_hp = set()

jenis_hp.add("pipo/vivo")
jenis_hp.add("oddo/appo")
jenis_hp.add("ipong/aphone")
jenis_hp.add(1212)#set juga bisa angka

print("jenis hp: ",jenis_hp)

# tapi himpunan juga bisa diurutkan caranya:
print('diurutkan: ',sorted(himpunan_kucing)) # sorted ini akan mengurutkan sesuai abjad(jadi tak bisa digabung dengan angka)

print('-'*20)
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {1,2,3,5,7}

print(ganjil.union(genap)) # union adalah untuk menggabungkan himpunan
print(ganjil.intersection(prima)) # intersection adalah irisan gunanya untuk mengambil data yang sama
