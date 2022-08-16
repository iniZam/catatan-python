import pygame

# step membuat game
# init
# user input, database input
# update asset
# render ke display
pygame.init()

# variabel runing game 
jalan = True


# membuat display/ tampilan sebagai aset game
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_panjang,window_lebar))


# object game
# posisi (ini konsepnya sama dengan diagram di mtk tu)
x= 250
y= 250
#ukuran 
panjang =20
lebar = 20
#kecepatan 
speed=1

while jalan: 
   # pygame.time.delay(10)# biar larinya gak terlalu kencang
    # user input, database input
    for event in pygame.event.get(): # ini adalah inputam dari user yang akan berguna untuk menutup program
        if event.type== pygame.QUIT:
            print ("anjay..........")
            jalan=False
    # ambil semua keyboard press(imputan keybiard)
    keys = pygame.key.get_pressed()
    #ambil ke kiri 
    if keys[pygame.K_LEFT] and x>0 :
        x-=speed
    # untuk ke kanan
    if keys[pygame.K_RIGHT] and x<window_lebar-lebar :
        x+=speed
    # untuk ke bawah
    if keys[pygame.K_DOWN] and y<window_panjang-lebar :
        y+=speed

    # untuk ke atas
    if keys[pygame.K_UP] and y>0 :
        y-=speed


    # update asset
    window.fill((255,255,255))# yang di dalam kurung itu rgb(warna)
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))# ini akan menggambar sebuah kotak sesuai dengan variabel yang sudah dideklarasikan di atas

    # render ke display
    pygame.display.update()
            
pygame.quit()# ini akan mengeluarkan dari window sesuai dengan user inputnya

