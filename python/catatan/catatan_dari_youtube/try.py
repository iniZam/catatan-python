try: # try ini akan mencoba program dibawahnya dan jika programnya error(selama bukan eror syntak) maka dia akan mengabaikan error dan lanjut ke exept
    a = 1/0 # satu tidak bisa dibagi dengan nol jadi ini adalah error yang bukan error syntak
except: # ini akan melanjutkan program jika bagian yang diketik di try mengalami error (selama bukan error syntak)
    print('error')

print('program masih jalan')
print("="*20)
#contoh lain
print("pembagian")
while True:
    try:
        angka1 = int(input('massukan angka: '))
        angka2 = int(input("masukan satu angka lagi"))
        hasil = angka1/angka2
        break
    #except Exception as err: #ini adlah versi lebih sederhana untuk menampilkan error seperti di line 18-21
    #    print(err) # tapi dia pake bahasa inggris kalo mo tes silahkan hapus tanda pagar di depan saja
    except ValueError: # ini akan dijalankan jika bukan angka yang dimasukan
        print('angka soe....!!!!!\nulang...!!!\n')
    except ZeroDivisionError: # ini akan dijalankan jika angka yang dimasukan 0 atau errornya seperti di line 2
        print(angka2,'tara bisa digunakan nanti pembagiannya error\nsilahkan coba lagi')

print("hasil dari pembagian",angka1,'dan',angka2,"adalah:",hasil,"\npembagian berhail. \nwidirit yey.....")

'''
    jenis-jenis error selain error sintak yang bisa dihandel exept
    1.IOError # ini error input ouput seperti saat buka file terus filenya corrupt (rusak/sejenisnya)
    2.ImportError # jika modul yang dimasukan/di import tidak ada
    3.ValueError #ini ada di line 18
    4.Division bt Zero# ini ada di line 20
    5.KeybiardInterupted
    6.EOFError
'''