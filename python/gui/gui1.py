import tkinter as tk
r = tk.Tk()
r.title('asu')
button = tk.Button(r, text='barenti da', width=25, command = r.destroy)
button.pack()
tombol = tk.Button(r, text = 'jalan',width= 40 , command = r.destroy)
tombol.pack()
r.mainloop()


#Bg : untuk mengatur warna background normal
#Command :  untuk memanggil function
#Font : untuk mengatur font pada label button
#Image : untuk menambahkan gambar pada button
#Width : mengatur lebar button
#Height : mengatur tinggi button

