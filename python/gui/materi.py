from tkinter import *

root = Tk()
root.geometry("500x200")
no = Label(root,text="No",padx=40)
nama = Label(root,text='nama')

no.grid(column=0,row=0)# grid ini untuk posisinya
nama.grid(column=1,row=0) # posisinya ini diatur kaya tabel

no1 = Label(root,text="1",fg="blue" ,bg="black")# fg adalah warna tulisan dan bg adalah warna background
nama1 = Label(root,text="anak asu",padx=30,pady=0,bg="black")# padx adalah ukuran horizontal(memanjang) dan pady adalah ukuran vertikal(kebawah)
no1.grid(column=0,row=1)
nama1.grid(column=1,row=1)

tengah = Label(root,text="tengah..")
tengah.grid(columnspan=2)# columnspan ini akan meletakannya di tengah antara column

mainloop()