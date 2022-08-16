print('string','='*20)
txt = ' halu semuanya apa kabar '

print(len(txt)) # len gunanya untuk mengecek panjang / jumlah charakter sebuah data

a = txt[1] # ini untuk mengabil character pertama dari variabel txt sesuai dengan index
print ('a',a)

b = txt[2:5] # ini untuk mengabil charracter di indeks tertentu termasuk spasi
print('b',b)

c = txt.strip() # ini untuk menghilangkan spasi pada awal dan akhir data
print('c', c)

d = txt.upper() # ini untuk mengubahnya menjadi huruf kapital 
print('d',d)

e = d.lower() # ini untuk mengubahnya menjadi huruf kecil
print('e',e) 

f = e.replace("s","w") # ini untuk mengganti salah satu huruf atau lebih
print('f',f)

age = [36,12,12,13]
txt = "halo aku si kampret dan umurku {}" # tanda {} gunanya uuntuk menampung variabel agen 
print(txt.format(age))

print(10>9)

