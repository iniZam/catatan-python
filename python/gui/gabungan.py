import tkinter as tk
from tkinter import *
from functools import partial
root = Tk()
root.geometry('500x600')

class aplikasikalkulator (tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('kalkulator tkinter')
        self.membuattombol()
        self.penentu = False

    def membuattombol(self):
        self.layar = tk.Entry(self,width=25)
        self.layar.grid(row=0,column=0,columnspan=5)

        btn_list = [
            '1','2','3',
            '4','5','6',
            '7','8','9',
            '0','+','-',
            'C','/','*',
            '='
        ]
        baris = 1 
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung,penampung)
            if (penampung == '='):
                tk.Button(self,text='=',width=22,command=perintah).grid(row=baris,column=kolom,columnspan=5)
                
            else:
                tk.Button(self,text=penampung,width=5,command=perintah).grid(row=baris,column=kolom)
                
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung (self,key):
        if key == '=':
            self.penentu = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0,tk.END) 
                self.layar.insert(tk.END,str(result))
            except:
                self.layar.insert(tk.END,"-> Error!")
        elif key == 'C':
            self.layar.delete(0,tk.END)
        else:
            if self.penentu :
                self.layar.delete(0,tk.END)
                self.penentu = False
            self.layar.insert(tk.END, key)


def jendelabaru ():
    Tk()

def tombol ():
    tekan =Button(text='asu')
    tekan.pack()

def baru():
    q = Label(text='kamu kampret')
    q.pack()

def pilihan ():
    ee = Tk()# ini buat jendela baru saat fungsi dipanggil
    v = IntVar()
    a= Label(ee,text='pilih emih kesukaanmu')# ini labelnya
    a.pack()
    b=Radiobutton(ee, text='Mie kuah', variable=v, value =1).pack(anchor=W)
    c=Radiobutton(ee, text='Mie goreng', variable=v, value =2).pack(anchor=W)
    b.pack()
    c.pack()

def angka():
    a = Tk()
    v = Spinbox(a,from_ =0, to = 10000000000000000)
    v.pack()



def menukecil():
    menu = Menu() #ini agar setiap memanggil variabel menu maka akan memanggil class menu juga dari tkinter
    root.config(menu=menu) # ini untuk kase muncul menu kecil di atas
    filemenu =Menu(menu)
    menu.add_cascade(label='file',menu=filemenu) # add_cascade gunanya untuk menambahkan tombol kecil di atas
    filemenu.add_command(label='spinbox',command=angka)# add_comand gunannya untuk menambahkan tombol di dalam tombol kecil yang sudah diletakan sebelumnya
    filemenu.add_command(label='baru....',command=jendelabaru)# ini juga fungsinya sama seperti di line 8
    filemenu.add_command(label='asas',command=pilihan)
    filemenu.add_command(label="kalkulator",command=aplikasikalkulator)
    filemenu.add_separator()# separatoe \\

    filemenu.add_command(label = 'keluarlah..............',command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='tolong....!!!',menu=helpmenu,command=tombol)
    helpmenu.add_command(label='About',command=baru)

menukecil()
mainloop()