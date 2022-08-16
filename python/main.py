
	# Luas = sisi*sisi
	# return Luas 

# def Luas_segitiga (alas,tinggi):
# 	Luas = (alas*tinggi)/2
# 	return = Luas

def Luas_lingkaran (jari_jari):
	Luas = float(3.14 * (jari_jari**2))
	return Luas

print ("mengitung luas lingkaran")
a = input ("masukan angka :")

hasil =  Luas_lingkaran(a)
print(hasil)

