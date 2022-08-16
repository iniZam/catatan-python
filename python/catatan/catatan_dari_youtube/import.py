# catatan : ini di command/dimatikan ini kalau mau di run tinggal hapus saja tanda pagar/hastagnya(#)
#import module # import ini gunanya untuk menggabungkan beberapa script atau memasukan 1 script ke script lain
#module.tambah(3,5) # cara untuk menggunakan fungsinya adalah dengan rumus (namamodul.fungsi/class)
#module.kurang(2,2)

#import module as m # ini untuk meringkas script yang dipanggil jadi nanti kalau mau panggil tinggal bikin seperti di line 7-8
#m.tambah(4,8)
#m.kurang(99,98)

from module import tambah,kurang # ini untuk kalo cuman mau pake def/class tertentu saja tapi jika ingin mengambil semuanya take saja tanda bintang(*) seperti pada line 11
#from module import tambah,kurang
tambah(88,12)
kurang(90,67)
