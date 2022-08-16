class Hero :

	# private class variabel
	__jumlah = 0

	def __init__(self,nama):
		self.nama = nama
		Hero.__jumlah += 1

	# method ini hanya berlaku pada objek sedangkan __jumlah ada nempel ke class
	def getjumlah (self):
		return Hero.__jumlah

	# method ini hanya berlaku di class
	def getjumlah1 ():
		return Hero.__jumlah

	@staticmethod # ini adalah static method yang berlaku pada class dan objek
	def getjumlah2():
		return Hero.__jumlah

	@classmethod # ini agar def nya itu nempel ke class saja
	def getjumlah3 (asu): # dalam kurung ini bisa isi apa saja tapi nanti kase sesuai dengan dibawahnya
		return asu.__jumlah

penembak = Hero('bambang')
print(Hero.getjumlah2()) # jadi mau panggilnya dari class Hero
pemukul = Hero('tukang pukul')
print(pemukul.getjumlah2()) # atau dari nama heronya maka dia akan tersambung/terhubung
setan = Hero('suanggi')
print(Hero.getjumlah3())