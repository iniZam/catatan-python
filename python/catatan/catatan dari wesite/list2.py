makanan =['nasi','ikan','buah','sayur']

w = len(makanan) # untuk mengecek panjang list
print(w)

# for x in makanan:
#     print(x)
makanan.append('asu')
makanan.append(20)
print(makanan,'append')# ini untuk menmbahkan list)

print(makanan.pop(1),'pop') # ini akan menghapus anggota list sesuai dengan indeksnya)

makanan.remove('asu')
print(makanan,'remove')# kalo ini akan menghapus salah satu datanya

telan= makanan.copy() # ini akan mengcopy isi list ke list lain
print(telan,'copy')
t = [1,2,3,4,5,6,7,8,9]
z=t.count(2)
print(z,'count')
print(makanan.clear())# ini akan mengosongkan list
