# tipe tipe data di python:
# integer(int) : tipe data untuk bilangan bulat
# float : tipe data untuk bilangan pecahan (bilangan yang ada komanya)
# string(str) : tipe data untuk huruf dan kalimat, bisa di isi dengan angka tapi angka itu tetap akan dianggap huruf dan kalimat sehingga data string tidak bisa digunakan untuk operasi bilangan/operasi aritmatika
# boolean (bool) : tipe data yang isinya cuman true dan false

# ini adlah program sederhana untuk mengetahui angka genap/ ganjil
x = int(input('masukan angka yang mau di cek:'))
y= x/2
if (y == int(y)): # jadi jika y mengahasilkan float(pecahan/ada komanya )maka baris dibawah ini akan diesekusi 
    print ("angka yang dimasukan adalah genap")
else : # jika y tidak menghasilkan int/bilangan bulat(tidak memenuhi syarat di line 10) maka baris ini ini yang akan dieksekusi
    print('angka yang dimasukan adalah ganjil')

angka = 9
tes = angka > 10

if angka == True :
    print(tes, 'maka angka',angka , 'lebih dari dari 10')
else :
    print(tes, 'maka angka',angka , 'kurang dari dari 10')
