import tkinter 

main_window = tkinter.Tk()

print(main_window.__dict__)

label1 = tkinter.Label(main_window, text = "asu")
label1.pack()

main_window.mainloop()