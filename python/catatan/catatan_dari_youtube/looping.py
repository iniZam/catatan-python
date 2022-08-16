# looping pada list
warna_kucing = ["oren",
                "abu-abu",
                'hitam',
                'putih',"pelangi"]
kelakuan = ["bar-bar","menjengkelkan","suka ngajak oren berantem","kawai njer wkwkwk :)"]

v = 1
for kucing in warna_kucing:
    print(v,"warna kucing",kucing)
    v+=1

#enumarete
print('-'*20)
print('berikut adalah warna kucing')
for i,cing in enumerate(warna_kucing): # ini adalah versi simpe dari line 7-10 dengan menggunakan enumarete
    print(i,cing)

# zip = untuk menggabungkan list bisa digunakan pada list dan tuple

for kocheng,sikap in zip(warna_kucing,kelakuan): # ini sintaknya kalo mau cuman 1 juga bisa kalo mau lebih juga bisa yang penting pisahkan dengan koma
    print("kucing warna",kocheng,"kelakuannya",sikap) # pastikan listnya baerurutan, dan yang ditampilkan hanya yang ada pasangannya kalo dia jomblo maka dia tak akan di print

# looping pada data set(himpunan)
print('set/himpunan\n','.'*20)
apasaja = {'laptop','kucing','ayam','garam','hp','bambang'}

for random in sorted(apasaja):
    print(random)

# looping pada dictonary
print('dictonary\n','.'*20)
apasaja2= {"oren":"bar-bar",
                "abu-abu":'menjengkelkan',
                'hitam':'kotu',
                'putih':'lucu aku suka :)',}

for i in apasaja2.items(): # yang dilooping ini keysnya, bisa juga diganti dengan value. kalo mau ambil semua pake items
    print(i)
print('='*20)
for n,m in apasaja2.items(): # ini mirip zip di line  tapi ini pake data dictonary
    print(n,"kelakuannya ",m)