def tambah (a,b):
    print('fungsi tambah')
    print(a,'+',b,'hasilnya:')
    return a+b

def kurang (a,b):
    print('fungsi kurang')
    print(a, '-', b, 'hasilnya:')
    return a-b


#print(__name__) # ini jika dipanggil dari file aslinya nanti ouputnya jadi __main__
                # tapi jika modul ini di import dan dipanggil dari modul lain maka ouputnya akan menujukan lokasi script ini
def main():
    print('ini adalah funsi utamanya matematika')

if __name__ == '__main__': # tuhuannya agar fungsi main ini hanya akan dijalankan jika di rund dari modul mtematika dan jika di run dari modul lain maka fungsi main tidak akan dijalankan
    main()