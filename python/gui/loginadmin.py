from tkinter import *
from tkinter import messagebox # ini dalah kotak pesan 

root = Tk()# ini untuk rampilannya
root.title('login admin')
root.geometry('300x110')# ini ukurannya

username = 'user'#ini variable user
sandi = '12345678'#ini variabel sandi



def login ():# ini adalah fungsi 
    user = e1.get()# get ini untuk mengambil apa yang sudah di isi di e1(line 24-26)
    pas = e2.get()# get ini untuk mengambil apa yang sudah di isi di e2(line 28-30)

    if (username == user and sandi == pas):
        messagebox.showinfo('halaman 1','halu......')#ini akan muncul kalau sandinya benar
        # isi dari messegebox : showinfo (ada di line 16), showerror(ada di line 19), askquestion,askokcancel,askyesno(ini nanti menyanyakan yes/no)
    
    elif(len(sandi) > 8):
        messagebox.showinfo ("peringatan....!!!!","sandi minimal harus 8")

    else :
        messagebox.askretrycancel ('gagal','anda gagal')# ini akan muncul kalo sanidnya salah

e1 = Entry(root)# entry ini adalah kotak kosanong untuk isi sesuatu
e1.pack()
e1.insert(0,'user')# insert ini untuk isi dia pe kotak kosang
label = Label(root,text='tempat login')
label.pack()


e2 = Entry()
e2.pack()
e2.insert(0,'sandi')# insert ini untuk isi dia pe kotak kosang

kotakbaru = Entry()
kotakbaru.pack()

# ini tombol 
tombol = Button(text='login',command=login)
tombol.pack()# ini untuk menampilkan tombolnya 

root.mainloop()