import tkinter 
from tkinter import *

main_window = tkinter.Tk()
#pertanyaannya
soal2 = 'Mie kuah atau mie goreng'
soal1 = 'pilih user(pengguna yang mau digunakan) :'
#jawabannya
jawaban1 = 'USER INI'
jawaban2 = 'USER ITU'

tombolsubmit = tkinter.Button(main_window,text='masukan')

def ini ():
    Label1 = tkinter.Label(main_window, text='ok sekarang kamu sudah masuk sebagai user ini\n tolong isi angkanya:\n')
    Label1.pack()
    v = Spinbox(from_ =0, to = 10000000000000000)
    v.pack()
    tombolsubmit.pack()
    
def itu ():
    Label2 = tkinter.Label(main_window,text='ok sekarang kamu akan dianggap sebagai user itu\ntolong pilih salah satu')
    Label2.pack()
    v= IntVar()
    N1 = Radiobutton (text='mie kuah',variable=v,value=1)
    N2 = Radiobutton (text='mie goreng',variable=v,value=2)
    N1.pack()
    N2.pack()
    tombolsubmit.pack()
    
# ini pertanyaannya
pertanyaan1 = tkinter.Label(main_window, text=soal1)# ini pertanyaannya
pertanyaan1.pack()


def tombol():
    tombol1 = tkinter.Button(main_window,text= jawaban1, command= ini)
    tombol2 = tkinter.Button(main_window,text= jawaban2,command= itu)
    tombol1.pack()
    tombol2.pack()
tombol()

tombol_keluar = tkinter.Button(main_window, text= '\nkeluar',command= main_window.destroy)
tombol_keluar.pack(side=BOTTOM)

main_window.mainloop()