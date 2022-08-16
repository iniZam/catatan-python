from tkinter import *
master = Tk()
w = Canvas(master,width=400, height=600)
w.pack()
Canvas_height=200
Canvas_width=2000
y = int(Canvas_height/2)
w.create_line(0,y, Canvas_width, y)

mainloop()

# bd: untuk mengatur lebar border dalam piksel.
# bg: untuk mengatur warna latar belakang normal.
# Cursor : untuk mengatur kursor yang digunakan di kanvas.
# Highlightcolor : untuk mengatur warna yang ditunjukkan dalam sorotan fokus.
# Width : untuk mengatur lebar widget.
# Height : untuk mengatur tinggi widget.