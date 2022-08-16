#loopign while
# Rumus while
# while argument(syarat) : # jadi selama argument yang ada di baris ini terpenuhi
# 		statement(pekerjaanya)	# maka statement ini akan selalu dilakukan sampai argumentnya tidak terpenuhi

# part 1
bilangan = 0
start = True
while start :
	print('masih :',bilangan,'.\tbelum sampe 20') # \t ini untuk memberi jarak. fungsinya mirip seperti tombol tab di keyboard
	if bilangan ==20: # ini saat bilangan so samoe 20s maka. jadi selama bilangannya belum sampai 100 maka ini tidak akan di jalankan 
		start = False # start yg di atas sudah jadi fale
		print ('sudah sampai',bilangan)
	bilangan += 1 # ini maksudnya adalah tambahkan 1 atau ini adalah versi sederhana dari line 4. dan ini akan terus berulang
#part 2
angka = 0
while angka<5:  
	if angka ==4:
		print ('cekpoint 1')
		# break dan continue di line 16 dan 17 ini di matikan(tidak akan dijalankan) kecuali dihapus tanda pagarnya(#)
		angka += 1 # tapi kalo baris ini di dihidupkan(dihapus tanda #) maka continue tidak akan menjadi looping berulang
		#break # break ini akan menghentikan looping dan keluar dari looping
		continue # ini akan terus mengulangi looping. maksudnya setelah baris ini dia akan terus menjalankan yg di atas(line 12-14)dan tidak akan menjalankan yang di bawah
		print ('cekpoint 2')# dari baris ini(line 17) sampai selsai looping(line 19) tidak akan di jalankan krena diatasnya ada break dan continue	 
	print ('asu',angka) # ini akan di print duluan baru dia jalankan yg di bawah
	angka = angka +1 # setelah itu variabel angkanya akan ditambhakan lalu dia ulang lagi di atas

else: # else ini akan mengambil hasil akhir dari perulanngan while di atas
	print(angka,"ini sudahh diluar while") # dan ini akan nge-print hasil dari elsenya
