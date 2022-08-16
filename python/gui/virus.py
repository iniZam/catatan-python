from tkinter import *

a = Tk()

kalimat = """
jadi ini adalalah sebuah string yang dimasukan ke variabel kalimat
jadi pada zaman dahaulu kala hahah . wkwkwkwk
"""

def jendela_baru(): 
    halaman=Tk()   
    teks = Label(halaman,text=kalimat)
    teks.pack()
    
def baru():
    tekan = Button(text="tekan ini",command=jendela_baru)
    tekan.pack()
baru()

mainloop()