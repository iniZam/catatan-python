# enkapsulasi = gunanya agar memprotect/melindungi variabel intences atau class yang sudah di privat tidak dirubah sembarangan saat program masih berjalan 

class Hero :
	
	def  __init__(self,nama,nyawa,serangan):
		self.__nama = nama 
		self.__nyawa = nyawa
		self.__serangan = serangan

	# getter : ini adalah cara untuk memanggil variabel yang diprivat
	def ambilnama(self):
		return self.__nama

	def ambilnyawa(self) :
		return self.__nyawa

	#setter : ini untuk mensetting / mengatur 
	def diserang(self,serangan_lawan): # ini fungsi untuk mengurangi nyawa hero
		self.__nyawa -= serangan_lawan

	def buffserangan(self,jumlah_buff):
		self.__serangan += jumlah_buff

# awal dari game
koro_sensei = Hero("koro sensei",100,12)

print(koro_sensei.__dict__)

# game berjalan 

# print(koro_sensei.__nama) # ini adalah cara yang salah jika memanggil variabel yang di privat
print(koro_sensei.ambilnama()) # cara yang benar untuk memanggil variabel yang di privat adalah yang ini
print(koro_sensei.ambilnyawa())
koro_sensei.buffserangan(20) # ini untuk menambah nilai serangan dengan menggunakan metho di line 21
koro_sensei.diserang(10) # ini adalah proses mengurangi nyawa hero dengan menggunakan method diserang dari line 28
print(koro_sensei.ambilnyawa())
print(koro_sensei.__dict__)