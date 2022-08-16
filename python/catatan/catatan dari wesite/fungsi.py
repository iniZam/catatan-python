#contoh 1
def fungsi(): # ini adalah cara buat funsi beserya syntaxnya 
    print('ini adalah sebuah fungsi')

fungsi()# ini adalah cara untuk memanggil fungsi yang telah dibuat (jangan lupa pake dalam kurung)

def fungsi2 (planet): # dalam kurung ini adalah argumen dan jika ingin memanggil fungsi ini maka argumennya wajib di isi
    print('halu aku dari planet ',planet)
#contoh 2
fungsi2('bumi')# ini adalah cara isi argumen saat memanggil fungsi. jika argumennya lebih dari satu maka pisakan saja dengan koma
fungsi2('pluto')

# contoh 3
def fungsi3(namadepan, namabelakang):
  print(namadepan + namabelakang)
fungsi3("Bam", "bang") 
# fungsi3('AJG')# ini akan eror karena ada 2 argumen tapi yang di isi cuman 1

#contoh 4
def fungsi4(*identitas): # tanda bintang digunakan untuk mengisi argumen dengan ju,lah seenak jidat/ argumen dengan jumlah tak tentu
    print('halu aku '+identitas[0])#kurung siku akan mengambil argumen ke 2/ argumen indeks ke 2(catatan: indeks dimulai dari 0)
fungsi4 ('kpopers garis keras','bocil jedag jedug','wibu')

#comtoh 5
def fungsi5(nama3,nama2,nama1):# argumen juga bisa dengan valuenya jika ingin 
    print('namaku  ',nama2) # ini menggunakan argumen nama2
fungsi5('ereh','hmmm','bambang') # walaupun argumennya tidak digunakan tapi jika argumennya ada maka nilainya harus di isi

#cintoh 6
def fungsi6 (**identitas):
    print('namaku adalah ',identitas["nama2"]) # ini agak mirip tapi beda dengan contoh 4. bedanya silahkan lihat sendiri saja
fungsi6(nama1='fatima',nama2='bambang')

#contoh 7
def fungsi7(negara = "Norway"): # argumennya sudah ada
  print("halu aku dari " + negara)

fungsi7("Sweden") # tapi argumennya juga bisa di timpa / digantikan dengan data baru
fungsi7() # kalo yang ini argumennya tidak diganti
fungsi7("Brazil") 

#contoh 8
def fungsi8(food):
  for x in food:
    print(x)
buah = ["apel", "pisang", "cheri","babi"]
fungsi8(buah)# argumen juga bisa sebuah variabel macam ni..........

#contoh 9
def fungsi9(x):
  return 5 * x # return ini
print(fungsi9(3))
print(fungsi9(5))
print(fungsi9(9))
print(fungsi9(5))
