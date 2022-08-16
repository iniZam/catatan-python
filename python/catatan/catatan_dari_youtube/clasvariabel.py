# ini part 1
class mahasiswa():
    
    jurusan = 'kelautan bikini bottom' # ini adalah variabel class
    def __init__(self,input_nama,input_id):
        self.nama= input_nama # variabel ini ada selfnya jadi dia adalah punyanya intences
        self.id= input_id

bambang = mahasiswa('bambang',23423) # ini intences
asu = mahasiswa('asu b*ngsat',23123)



bambang.jurusan= 'infrastruktur bikini bottom' # ini akan menimpa variabel class sehingga ini akan menjadi variabel intences 

# print(bambang.jurusan)
# print(mahasiswa.jurusan)

#print(mahasiswa.__dict__) # ini akan mengecek apa saja yang tersedia di class mahasiswa
#print(bambang.__dict__) # dict ini untuk mengecek apa saja variabel yang tersedia di bambang(variabel yang tersedia itu yang ada selfnya saja (line 5 dan 6) dan line 13 karena itu adalah variabel baru)

# ini part 2 ini adalah program sederhana yang menujukan gunanya variabel class
print('part 2')
class mahasiswa():
    
    jumlahmahasiswa = 0
    def __init__(self,input_nama,input_id):
        self.nama= input_nama # variabel ini ada selfnya jadi dia adalah punyanya intences
        self.id= input_id
        mahasiswa.jumlahmahasiswa += 1 # ini gunaya agar setiap buat 1 data mahsiswa menggunakan class mahasiswa maka jumlah mahasiswanya akan bertambah 1

bambang = mahasiswa('bambang',23423) # ini intences
asu = mahasiswa('asu b*ngsat',23123)

print('jumlah mahasiswa: ' ,mahasiswa.jumlahmahasiswa)