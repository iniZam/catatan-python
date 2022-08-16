import art
from art import tprint
restart = 'y'
kesempatan = 3
balances = 1000000


while kesempatan >= 0:
    pin = int(input("masukan pin anda tolong : ") )
    if pin == 1234:
        print ("pin yang anda masukan sudah benar")
        art.tprint("anjay !!!")
        print('''
        pilih salah satu pilihan di bawah ini
        1 untuk cek saldo
        2 untuk ambe doi
        3 untuk kase doi
        4 untuk kase kaluar/ ambe kartu
        ''')
        pilih = (input('pilih yang mana? '))
        if pilih == '1':
            print('sando anda sekarang adalah ', balances , '\n')
            restart = str(input("masih mau transaksi\nya atau tidak:"))
            if restart in ('y','ya','YA','Y'):
                    art.tprint("terima kasih")                
            else:
                    art.tprint("terima kasih")
                    break
        elif pilih == '2':
            # option2 = "y"
            print("1.Rp 50.000 \n2.Rp 100.000 \n3.Rp 200.000 \n4.Lainya....")
            tarik = int(input('berapa banyak uang yang mau diambil:'))
            if tarik == 1:
                tarikan = 50000
                balances = balances-tarikan
                tprint('penarikan berhasil')
                print('saldo yang ditarik ',tarikan)
                print('\nsekarang sisa saldomu adalah ',balances)
                restart = str(input("masih mau transaksi\nya atau tidak:"))
                if restart in ('no','n','NO','N'):
                    art.tprint("terima kasih")                
                    break       
            elif tarik == 2:
                tarikan = 100000
                tprint('penarikan berhasil')
                balances = balances-tarikan
                print('\nsekarang sisa saldomu adalah ',balances)
                restart = input("masih mau transaksi\nya atau tidak")
                if restart == ('no','n','NO','N'):
                    art.tprint("terima kasih")
                    break
                
            elif tarik == 3:
                tarikan = 300000
                tprint('penarikan berhasil')
                balances = balances-tarikan
                print('\nsekarang sisa saldomu adalah ',balances)
                restart = input("masih mau transaksi\nya atau tidak")
                if restart == ('no','n','NO','N'):
                    art.tprint("terima kasih")
                    break
                
            elif tarik == 4 :
                jumlah = float(input('masukan jumlah yang mau diambil'))
                balances = balances - jumlah
                tprint ('berhasil')
                print ('poenarikan berhasil \n sekarang sisa saldomu : ',balances)
                restart = input("masih mau transaksi\nya atau tidak")
                if restart == ('no','n','NO','N'):
                    art.tprint("terima kasih")
                    break
            else:
                tprint('salah...!!')
                print('pilihan yang anda pilih itu tidak ada jadi tolong masukan ulang')
                restart = 'y'
        elif pilih =='3' :
            bayar = float(input('berapa yang mau dibayar/disetot? \n'))
            balances = balances+bayar
            print('saldomu sekarang',balances)
            if restart == ('n','N','no','NO'):
                    tprint("terima kasih")
                    break
        elif pilih == '4' :
            print ('tunggu kartu kaluar e....')
            tprint ('terima kash :,)')
            break
        else :
            print('kase maso yang batul ')
            restart = 'y'
    elif pin != 1234:
            tprint('sandi salah')
            print('tolong masukan sandi anda')