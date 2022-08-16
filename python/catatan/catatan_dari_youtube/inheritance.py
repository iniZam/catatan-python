#inheritance adalah penurunan/ warian antar class. jadi jika sudah selesai buat sebuah class terus buat class baru yang mirip maka tra perlu copas dan pakai saja inheritance sehingga class baru bisa mengambil semua yang sudah ada di class sebelumnya
class ojek():
    
    def __init__(self,nama,dg,daerah) :
        self.nama = nama
        self.dg = dg
        self.daerah = daerah

    def cekojek(self):
        print('nama: ',self.nama,'\ndg motor',self.dg,'\ndaerahkeluyuran: ',self.daerah)

class ojekonline(ojek): # yang di dalam kurung adalah inheritance . jadi semua yang dimiliki oleh class ojek bisa diwariskan ke class ojelonline
    def cekojek(self): # kalo ada yang mau dibedakan dari variabel ojek maka timpa saja yang penting dia pe nama sama. kalo ada yang mau ditambahkan juga bisa ditambagkan
        print('asu') # ini menimpa fungsi cekojek dari class ojek dan membuat fungsi cek ojek yang baru


ojek1 = ojek('bambang',3431,'bulan')
ojek2 = ojekonline('naruto',2341,'isekai')

ojek1.cekojek()
ojek2.cekojek()