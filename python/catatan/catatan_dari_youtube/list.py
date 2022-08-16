#ini adalah datamya
data = [1,4,2,11,24,66,89,'ini string']
data1 = [200,543,678,'asu']
print('data=',data,'\ndata1=',data1)#\n =ini berfungsi seperti enter saat data di print
print('='*30)# ini nanti jadi tanda samadengan(=), ada banyak
#ini untuk mengakses list
datapanggilan = data[0]# ini adalah variabel untuk mengakses list dari index 0(yang paling depan)
datapanggilan1 = data[3]# ini mengakses list dari index 3(dimulai dari 0)
datapanggilan2 = data[-2]# ini mengakses list dari paling belakang(kalo dari belakang indexnya tidak dimulai dari 0 tapi dari 1)
potongdata = data[0:5]#ini akan mengakses list dari index 0 sampai sebelum index 5(index 0-4)
potongdata1 = data[:4]# ini mengakses list dari index 0 sampai sebelum index 4(index 3) atau bisa dianggap ini akan memanggil 4 data yang paling depan

#ini untuk memanipulasi data

#ini untuk menambah list
data2= data+data1  # ini menggabungkan list data dan data1

#ini untuk menyalin data
salinan = data[:]#tanda [:]ini berguna agar semua data yang ada di list data, disalin ke list salinan
salinan[4] = 65 # ini akan mengganti data di list salinan, index ke 4 dengan 65

# ini untuk merubah list
data2[4:9] = ['satu',1,56,900,99,'pam']# ini akan mengganti data dari list 4 sampai sebelum list 9(dari list 4 sampai list8)

#list dalam list
qwerty = [data,data1]
#cara mengakses list dalam list
a = qwerty[1][3] # ini akan mengkases list ke 1(mulainya dari 0) dan list index ke 3 

#method(fungsi) di list
data3 = data2[:]
data3.append(10)# append ini untuk menambah jumlah list
panjangdata = len(data3)# len ini untuk menunjukan panjang(jumlah listnya)


# ini adalah printnya 
print ('datapanggilan =',datapanggilan,'line7','\ndatapanggilan1=',datapanggilan1,'line 8','\ndatapanggilan2=',datapanggilan2,'line 9')# ini dipanggil dari line 8 dan 9
print('potongdata=',potongdata,'\npotongdata1=',potongdata1)#ini dipanggil dari line 11 dan 12
print('data2=',data2)# ini dipanggil dari line 17
print('data=',data,'\nsalinan=',salinan)# salinan dipanggil dari 20 dan 21. dan data dipanngil dari line 2
print('data=',data2)# ini dipanggil dari line24
print('qwerty=',qwerty)# ini dipanggil dari line 27
print('a=',a)# ini dipanggil dari line ke 28
print('data3 = ',data3)# ini dipanggil dari line 33
print('panjangdata3=',panjangdata)# ini dipanggil dari line 34

