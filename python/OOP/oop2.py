class hero : # ini adalah class/template atau bisa juga dibilang cetak biru. formulir program
	
	def __init__(self,input_nama,jumlah_nyawa,jumlah_serangan,jumlah_armor): # ini akan pertama kali dieksekusi saat classnya dipanggil. dan self di dalam kurungnya itu bisa dianggap adalah hero1
		self.nama= input_nama
		self.nyawa = jumlah_nyawa
		self.serang = jumlah_serangan
		self.armor = jumlah_armor

hero1 = hero("anak ajg",1200,120,200) # jadi variabel yang di depan sekali itu akan mengisi selfnya yang sudah dirancang di class hero
hero2 = hero("udin",1200,500,120) # jika class bisa dibilang formulir maka ini adalah cara mengisi formulirnya
hero3 = hero("asu",30000,20,290)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)