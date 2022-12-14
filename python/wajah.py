import arcade

#mengatur ukuran layar
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#membuka jendela baru dan mengatur nama jendela dan dimensinya(lebar dan tinggi)
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT , "DRAWING EXAMPLE" )

# Mengatur warna latar belakang menjadi putih
# Untuk daftar nama warna lihat:
# http://arcade.academy/arcade.color.html
# Warna bisa juga dipakai dalam format (red, green, blue) dan 
# (red, green, blue, alpha).
arcade.set_background_color(arcade.color.WHITE) # ini adalah backgroundnya 

# Mulai proses render. Harus ditulis sebelum perintah drawing.
arcade.start_render()

#menggambar wajah 
x= 300
y = 300
radius = 200
arcade.draw_circle_filled(x,y,radius, arcade.color.YELLOW)

# menggambar mata kanan
x = 370 
y = 350
radius = 20
arcade.draw_circle_filled(x,y,radius, arcade.color.BLACK)

#menggabar mata kiri
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x,y,radius, arcade.color.BLACK)

# menggabar senyum 
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)


# Menampilkan hasil gambar (drawing)
arcade.finish_render()

# Biarkan jendela terbuka sampai user menutupnya dengan tombol 'close
arcade.run()
