# private variabel 

class Hero :
	jumlah = 0
	__jumlahprivate = 0

	def __init__(self,nama,nyawa):
		self.nama = nama
		self.nyawa = nyawa

		#variabel intences private = variabel privat di dalam kelas yang tidak bisa dimanipulasi dan tidak bisa dipanggil
		self.__private = "privat"

		#variabel intences protected = masih belum dipahami cuman intinya dia ada 1 underscout saja 
		self._protected = "proted"

Naruto = Hero("Naruto",100)

print(Naruto.__dict__)

Naruto._protected = "tes"# kalo mau ubah variabel protec nanti jadinya malah buat variabel baru
print(Naruto._protected)
print(Naruto.__dict__)

Naruto.__private = "asu" # kalo mau coba ubah private nanti jadinya malah membuat variabel baru
print(Naruto.__private)
print('\n')
print(Hero.__dict__)
