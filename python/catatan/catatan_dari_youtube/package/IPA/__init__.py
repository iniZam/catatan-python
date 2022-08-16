# __init__ ini gunanya adalah agar setiap folder IPA di import maka modul ini akan otomatis dieksekusi
from .matematika import * # ini akan memanggil modul matematika sekaligus menggabungkan matematika dengan modul ini
from  .fisika import * #ini juga sama kayak di line 2 (titik itu memang sintaknya)

'''ini pada dasarnya mirip dengan tkinter dan tkinter dibuat juga dengan cara begini yaitu'''

print("ini dipanggil dari ,modul __init__")