from tkinter import *
root = Tk()
root.geometry('300x400')
v = IntVar()
a= Label(text='pilih emih kesukaanmu')
a.pack()
Radiobutton(root, text='Mie kuah', variable=v, value =1).pack(anchor=W)
Radiobutton(root, text='Mie goreng', variable=v, value =2).pack(anchor=W)
mainloop()

a= Label(text='jfdg')


