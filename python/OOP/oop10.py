class Hero :

	def __init__(self,nama,nyawa,armor):
		self.nama = nama
		self.__nyawa = nyawa
		self.__armor = armor
		# self.info = "nama {}: \n\tnyawa: {}".format (self.nama,self.__nyawa)# kurung kurawal ini gunanya untuk mengisi data dan format berguna untuk menentukan data yang mau di isi dan data yang di isi ini ada di line 4 dan 5

	@property # ini berguna agar sebuah method/fungsi/def dianggap sebagai sebuah variabel
	def info(self): # salah satu keunggulannya adalah jika ada yang diganti maka dia akan langsung ke update karena variabel itu dia gampang berubah
		return "nama {} : \n\t\t nyawa: {} \n\t\tarmor: ".format (self.nama,self.__nyawa,self.__armor) # ini pada sama saja dengan yang ada di line 7 tapi ini di isi di dalam sebuah method 
	
	# ini untuk mengambil dan menampilkan variabel yang sudah di privat
	def armor (self):
		return self.__armor

	# ini untuk mengatur/memanipulasi data/variabel agar variabelnya bisa diubah
	def armor (self,masukan):
		self.__armor = masukan

penembak = Hero("penembak handal",1000,10)


print(penembak.info) # ini akan memanggil self.info yang ada di line 7
penembak.nama = "asu" # ini akan merubah nama hero 
print("merubah info")
print(penembak.info) # ini akan memanggil self.info yang ada di line 7

print("getter dan setter untuk armor")


# print(penembak.armor)

