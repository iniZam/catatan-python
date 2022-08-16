# percabangan yg dimaksud ini itu adalah if elif dan else
''' 
catatan :
         sama dengan : ==
         kurang dari : <
         lebih dari : >
         kurang dari sama dengan : <=
         lebih dari sama dengan : >= 
         tidak sana : != 
'''

#contoh 1
a = 100
b = 10
if b <a : # jadi selama syarat ini terpenuhi maka ini akan dieksekusi dan jika syaraynya tidak terpenuhi maka if ini tidak akan dieksekusi 
    print ('b lebih kecil dari a')
if b == a:
    pass # pass ini tak ada gunanya. gunanya cuman untuk mengisi tempat saja agar tidak salah sintaknya
elif b!=a: # eliif itu sebenarnya sama saja dengan if. tapi elif akan dieksekusi jika syarat if tidak terpenuhi dan masih ada syarat lain 
    print ('b sama dengan a') 
else : # else dan dibawahnya ini akan dieksekusi jika tidak ada syarat di atas yang terpenuhi(else ini hanya bisa 1 tidak bisa lebih dari 1 di tiap contoh)
    print('tidak ada syarat yang terpenuhi') 

