from tkinter import *

root = Tk()# ini untuk jendelannya
def jendelabaru ():
    Tk()
menu = Menu() #ini agar setiap memanggil variabel menu maka akan memanggil class menu juga dari tkinter
root.config(menu=menu) # ini untuk kase muncul menu kecil di atas
filemenu =Menu(menu)
menu.add_cascade(label='file',menu=filemenu) # add_cascade gunanya untuk menambahkan tombol kecil di atas
filemenu.add_command(command=jendelabaru,label='baru')# add_comand gunannya untuk menambahkan tombol di dalam tombol kecil yang sudah diletakan sebelumnya
filemenu.add_command(label='open.....')# ini juga fungsinya sama seperti di line 8
filemenu.add_separator()# separatoe \\
filemenu.add_command(label = 'keluarlah..............',command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='tolong....!!!',menu=helpmenu)
helpmenu.add_command(label='About')

mainloop()