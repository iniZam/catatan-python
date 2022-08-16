a= int(input('masukan angka yang dicari:'))

#looping for

# rumus for 
# for x in range(0,30,2): # untuk range itu dalam kurungnya itu(awal,akhir,selisih) dan jika di isi cuman satu maka rangenya hanya ada batas atas
	# print (x) ini akan terus diulang sebanyak rangenya
for i in range(0,30,2):# jangan lupa untuk pake titik dua(:)
	print(i)
	if (i==a):
		print ('ketemu:',a)
		break # break ini akan menghentikan loopingnya sebelum selesai jika sudah memenuhi syarat 
else:# else ini akan dieksekusi jika looping fornya sudah selesai semua
	print('tara dapa')

print('='*20)#ini nanti jadinya kaya garis

for r in range(1,20):
	print (r)
	if r == a:
		print('angka ketemu :',r)
		continue# continue ini akan melanjutkan looping walaupun sudah memenuhi syarat

else :
	print('pencarian angka',a,' selesai')

for b in range(1,100):
	pass # ini tidak ada gunanya/ gunanya hanya untuk memenuhi aturan syntaxnya

for i in reversed(range(1,10,1)):# reversed ini akan menampilkan data secara terbalik
	print(i)


