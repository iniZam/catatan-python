# ques(antrian) = penumpuk yang keluarannya itu data yg lebih dulu di input
from collections import deque

print('-'*10,'ques/tumpukan','-'*10)
antrian = deque([10,20,30,40,50,79,90])
print('antrian sekarang',antrian)

#menambahkan antrian
antrian.append('bangsat kau')
print('tambahan: bangsat kau')
antrian.append(1945)
print('tambahan: ',1945)
print('data sekarang adalah',antrian)
#mengurangi antrian
out = antrian.popleft()#popleft ini akan mengeluarkan data yang posisinya paling kiri(data yang paling awal)
print('data keluar',out)
print('data sekarang adalah',antrian)
out = antrian.popleft()
print('data keluar',out)
print('data sekarang adalah',antrian)

# stack = penumpuk yang keluarannya itu dari yg terakhir di input
print('-'*10,'stack/antrian','-'*10)
tumpukan = [1,2,3,4,5,6,7]
print('data awal',tumpukan)
#memasukan data baru
tumpukan.append(7)
print('memasukan data baru:',7)
tumpukan.append(10)
print('memasukan data baru: ',10)
print('data sekarang',tumpukan)

keluar= tumpukan.pop()#ini akan menghilangkan data yang paling belakang
print('data yang dikeluarkan: ',keluar)
print('data sekarang',tumpukan,'\tini sudah diambil data yang paling akhir')
