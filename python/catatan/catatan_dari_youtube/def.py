def kerang (): # ini adalah fungsi atau bisa disebut mini modul. atau bisa disebut juga cabang program
	print('halu...\t ini dari fungsi di line 1')# jadi dari baris ini(line 2) sampai selesai akan masuk ke fungsi di line 1 dan tidak akan dijalankan kecuali fungsinya dipanggil di bawah

kerang()#ini memanggil fungsinya yang ada di line 1

# part 1(fungsi sederhana)
print('part 1','-'*30)
def harga_ginjal_ayam ():# jadi saat fungsi ini dipanggil maka semua yg ada di bagian bawahnya sampai selesai juga akan ikut terpanggil
	print('harga giljal ayam sekarang berada di kisaran 10.000 per ginjal')# yang ada di bawanya itu yg agak bajarak tu....

def pasar_gelap ():# jadi saat fungsi ini dipanggil maka semua yg ada di bagian bawahnya sampai selesai juga akan ikut terpanggil
	harga_ginjal_ayam()# ini akan memanggil fungsi harga_ginjal_ayam di line 8 dan fungsi print di line 9 juga ikut terpanggil

pasar_gelap()#ini akan memanggil fungsi di line 11

# part 2(fungsi dengan input argumen sederhana)
print('part 2 ','-'*30)
def harga_total_ginjal_ayam(biji): # biji adalah inputan argumen untuk fungsi di line ini
	harga_ginjal_ayam()
	harga = 10000
	Total = biji*harga
	print('harga',biji,'biji dari ginjal ayam adalah',Total,'Ribu')

harga_total_ginjal_ayam(12)# ini akan memanggil fingsi di lne 16. dan 12 yg ada di dalam kurung adalah inputan yang akan di masukan ke variabel biji yang juga ada di line 16

# part 3 (fungsi dengan keywords argumen)
print('part3','-'*30)
def manusia(nama,status): #keywords ini maksudnya jika argumennya mau di input tidak perlu sesuai dengan urutannya yang (contohnya lihat di line 33 dan line 34)
	print('manunsia ini bernama:',nama)
	print('sekarang statusnya :',status)

manusia(nama='Ihwan',status='dah mokad')
manusia(status='ditangkap karena pancuri cas-cas',nama='Riska')# ini contoh yang benar, jika di isinya tidak berurutan maka harus seperti line ini
manusia('dikutuk','abex') # ini contoh yang salah, karena kalau tidak pakai argumen seperti line 32 dan 33 maka harus berurutan
manusia('Zulfikri','nganggur')# contoh yang ini juga batul karena harus berurutan jika mau ditulis langsung

# part 4 (yang ini pake argumen default)
print('part 4','-'*30)

def mahluk(nama,jenis='orang',planet='bukan dari Bumi',ahlak='gak punya',gender='cwk'): # default itu maksudnya nilainya sudah di isi duluan(yang sudah ada jadi tidak perlu di isi), tapi yang belum di isi maka harus di isi dulu nilainya lihat contoh di line 47-49
	print('mahluk ini berjenis : ',jenis)
	print('mahluk ini bernama : ',nama)
	print('asal mahluk ini dari : ',planet)
	print('ahlaknya : ',ahlak)
	print('cwk/cwk?',gender)

mahluk('bambang')
mahluk('fatima',planet='mars')# walaupun argumennya default(sudah di isi duluan tapi masih bisa di ubah)
#mahluk(planet='pluto')# ini contoh yang salah karena argumen yang belum di isi di atas maka harus di isi dulu agar programnya jalan, jadi jika dijalankan maka akan error


# part 4 (fungsi dengan return)
print('part 4','-'*30)
def pangkat(angka):
	Total = angka **2
	print ('hasil pangkat 2 dari',angka,' adalah ',Total,'-'*5,'ini dari fungsi pangkat, dari line 55')
	return Total # return ini gunanya agar variabel di dalam fungsi ini bisa dupanggil dari luar 


asu = pangkat(4)# ini memanggil fungsi dari line 53 sekaligus memasukannya ke variabel asu
print (asu,'-'*5,'ini adalah hasil dari memanggil return')# ini hanya memanggil return dari line 57

#part 5  fungsi dengan argumen lebih dari 1
print ('part 5','-'*30)

def tambah (angka1,angka2): # ini kurang lebih sama saja dengan part 4 tapi inputan argumennya ada 2
	hasil = angka1+angka2
	print (angka1,'+',angka2,'=',hasil)
	return hasil

def kali (angka1,angka2): # yang di dalam kurung adalah argumen
	hasil = angka1*angka2 # dari baris ini(line 72) dan di seterusnya(line 74) adalah statement
	print (angka1,'x',angka2,'=',hasil)
	return hasil 

anj = tambah(9,10)
ing = kali(3,anj)# argumen di dalam kurung tidak harus selalu angka bisa juga variabel yang penting masih memenuhi syarat

print(anj)
print(ing)
