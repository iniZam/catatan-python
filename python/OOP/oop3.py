class Hero : # ini adalah class/template atau bisa juga dibilang cetak biru. formulir program
	
	jumlah = 0#ini adalah class varaible dan akan nempel di classnya

	def __init__(self,input_nama,jumlah_nyawa,jumlah_serangan,jumlah_armor): # ini akan pertama kali dieksekusi saat classnya dipanggil. dan self di dalam kurungnya itu bisa dianggap adalah hero1
		self.nama= input_nama # ini adalah intences variabel dan hanya akan terpanggil jika variabelnya dipanggil juga
		self.nyawa = jumlah_nyawa
		self.serang = jumlah_serangan
		self.armor = jumlah_armor
		Hero.jumlah += 1 # ini akan menamnah variabel jumlah setiap classnya dipanggil atau menambah hero
		print("hero dengan nama ",input_nama, "sudah selesai dibuat")

hero1 = Hero("anak ajg",1200,120,200) # jadi variabel yang di depan sekali itu akan mengisi selfnya yang sudah dirancang di class Hero
print(Hero.jumlah)
hero2 = Hero("udin",1200,500,120) # jika class bisa dibilang formulir maka ini adalah cara mengisi formulirnya
print(Hero.jumlah)
hero3 = Hero("asu",30000,20,290)
print(Hero.jumlah)
