# dictonary adalah struktur data yang menggunakan maping
# rumus dictonary:
# kucing1 = {key:value,key:value}

kocheng1 = {"ID":232,
            "nama":"bambang",
            "kerja?":"ngak dia cuman makan saja",
            "warna" : "itam putih",
            "makan":"wiskas"}
kocheng2 = {"ID":233,
            "nama":"bon",
            'kerja?':"ya kali cubing kerja",
            "warna":"oren",
            "makanan":"wiskas juga"}



#cara memanggil data tipe dictonary
print(kocheng1["nama"],'\tini dipanggil dengan keys nama') # dictonary ini bisa dipanggil dengan cara memanggil keys nya. beda dengan list yang pake index
print(kocheng1.keys(),'\tini keys') # ini akan memanggil semua keys nya
print(kocheng1.values(),'\tini value') # ini akan memanggul semua valuenya
print(kocheng1.items(),'\tini items') # ini akan memanggil items

kucing_list = {232:kocheng1,233:kocheng2} # seperti membuar dictonary di dalam dictonary
print(kucing_list[233]) # ini akan mengeluarkan data tentang kucing dengan ID 232
