import tkinter as tkr
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

import os
from tkinter.messagebox import askokcancel

root = tkr.Tk()

class SimpleEditor (tkr.Frame):
	def __init__ (self,parent=None, file=None):
		tkr.Frame.__init__(self, parent)
		self.frm = tkr.Frame(parent)
		self.frm.pack(fill=tkr.X)
		self.layoutKolom = tkr.Frame(root)
		self.buatNamaFile()
		parent.title("pam param pam pam. pam pam")
		self.buatTombol()
		self.kolomTeksUtama()
		self.indeks = 1.0
		self.path = ''

	def buatTombol(self):
		tkr.Button(self.frm, text = 'Buka....',command=self.openFile).pack(side=tkr.LEFT)
		tkr.Button(self.frm, text = 'simpan', command=self.perintahSimpan).pack(side=tkr.LEFT)
		tkr.Button(self.frm, text = 'kaluar', command=self.perintahKeluar).pack(side=tkr.LEFT)


	def kolomTeksUtama(self):
		scrool = tkr.Scrollbar(self)
		kolomTeks = tkr.Text(self, relief = tkr.SUNKEN)
		scrool.config(command=kolomTeks.yview)
		kolomTeks.config(yscrollcommand =scrool.set)
		scrool.pack(side=tkr.RIGHT, fill=tkr.Y)
		kolomTeks.pack(side=tkr.LEFT, expand=tkr.YES, fill=tkr.BOTH)
		self.kolomTeks = kolomTeks
		self.pack(expand=tkr.YES, fill = tkr.BOTH)

	def perintahSimpan (self):
		print(self.path)
		if self.path:
			alltext = self.gettext()
			open(self.path,'w').write(alltext)
			messagebox.showinfo('berhasil', 'file so aman')
		else:
			tipeFile = (['Text File',('*txt'),('Python file','*.py'),'All files','.*'])
			filename = asksaveasfilename(filetypes=(tipeFile))
			if filename:
				alltext = self.gettext()
				open(filename, 'w').write(alltext)
				self.path = filename
	def perintahKeluar(self):
		ans = askokcancel('kaluar','batul mo kaluar to?')
		if ans:
			tkr.Frame.quit(self)

	def settext(self, text='',file=None):
		if file:
			text = open (file, 'r').read()
		self.kolomTeks.delete('1.0',tkr.END)
		self.kolomTeks.insert('1.0',text)
		self.kolomTeks.mark_set(tkr.INSERT,'1.0')
		self.kolomTeks.focus()

	def gettext(self):
		return self.kolomTeks.get('1.0',tkr.END+'-1c')

	def buatNamaFile(self):
		self.layoutKolom.pack(fill=tkr.BOTH, expand=1, padx=17, pady=5)

	def openFile(self):
		eksistensiFile = [('All files','*.*', ('text Files', '*.txt'),('Python files','*.py'))]
		open = filedialog.askopenfilename(filetypes=eksistensiFile)
		if open != '':
			text = self.readFile(open)
			if text:
				self.path = open
				#nama = os.path.basename(open)
				self.kolomTeks.delete('1.0',tkr.END)
				self.kolomTeks.insert(tkr.END,text)

	def readFile(self,filename):
		try:
			f = open(filename,'r')
			text = f.read
			return text
		except :
			messagebox.showerror('tra jadi !!')
			return None

SimpleEditor(root)
tkr.mainloop()