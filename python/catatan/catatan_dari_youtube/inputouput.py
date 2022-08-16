# membuat file external

'''
w = write / mode monulis dan menghapus file lama, jika filenya bellum ada maka akan mebuat file baru 
r = rean only / hanya membaca file
a = append / menambahkan data di akhir baris
r+ = write dan read mode
'''
# membuat file text
file = open("wow.txt","w")# ini argumennya ada 2 yaitu nama file dan mode

file.write("padazamandahulu1812/padazamandahulu1218")
file.write('\nini baris kedua')
file.write('\nini baris ketiga')
file.write('\nini baris keempat')
file.write("\n2a:54:0e:1e:e0:dd")
file.close() # jangan lupa di close

# membaca file
file2 = open("wow.txt",'r')

# print(file2.read(10)) # bagian dalam kurungnya bisa di isi dengan jumlah karakter yang mau di baca
# print(file2.readline())
file2.close()

# appending

file3 = open('wow.txt','a')

file3.write =('ini dari dari mode append')
file3.close() 