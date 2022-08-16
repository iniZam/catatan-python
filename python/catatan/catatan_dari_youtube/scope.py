# scope variabel : lokal

manusia = 'bambang' # ini adalah variabel global (maksudnya bisa langsung di akses)
makananorang = 'nasi'

print('lokal','-'*20)
def gantinama(namabaru):
    namasikampret = namabaru # ini adalah variabel lokal. maksudnya variabel ini sudah berada di dalam fugsi ini dan hanya bisa diakses dengan memanggil fungsinya
    print('selamat nanamu sudah diganti dari ',namasikampret)

gantinama('asu')
# print('dan namamu sekarang jadi: ',namasikampret) # ini tak bisa dipanggil karena variabel namasikampret adalah variabel lokal

# scope variabel : global
print('global','-'*20)
def gantinama(namabaru):
    global namasikampret # ini gunannya agar variabel lokal di dalam fungsi ini bisa berubah menjadi variabel global
    namasikampret = namabaru # ini adalah variabel lokal
    print('selamat nanamu sudah diganti dari ',manusia)

gantinama('asu')
print('dan namamu sekarang jadi: ',namasikampret)
print('-'*20)

def jatahmakan(makanan,nama):
    global namasikampret,makananorang # kalo variabel yang mau di globalkan ada banyak maka tinggal tulis saja tapi jangan lupa pisahkan dengan koma
    namasikampret = nama # ini gunanya agar variabel namasikampret mengakses variabel nama dan data selanjutnya bisa berubah
    makananorang = makanan # ini gunanya agar variabel makananorang mengakses variabel makanan dan data selanjutnya bisa berubah

jatahmakan('emmieh','alek')

print('namamu sekarang jadi: ',namasikampret,'dan makanan sehari-harimu adalah',makananorang)
