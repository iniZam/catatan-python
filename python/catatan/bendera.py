import turtle

bendera = turtle.Turtle()

# tiangnya
bendera.color("brown")
bendera.begin_fill()
bendera.forward(10)
bendera.left(90)
bendera.forward(300)
bendera.left(90)
bendera.forward(10)
bendera.left(90)
bendera.forward(300)
bendera.end_fill()

#geser kursor
bendera.penup()
bendera.left(90)
bendera.forward(10)
bendera.left(90)
bendera.forward(300)
bendera.pendown()

#bendera merah
bendera.color("black","red")
bendera.begin_fill()
bendera.right(90)
bendera.forward(200)
bendera.right(90)
bendera.forward(50)
bendera.right(90)
bendera.forward(200)
bendera.end_fill()

# bendera putih
bendera.color("black","white")
bendera.left(90)
bendera.forward(50)
bendera.left(90)
bendera.forward(200)
bendera.left(90)
bendera.forward(50)
bendera.left(90)
bendera.forward(200)
bendera.end_fill()

bendera.penup()
bendera.left(90)
bendera.forward(50)
bendera.pendown()

bendera.penup()
bendera.left(45)
bendera.forward(200)
bendera.right(90)
# bendera.forward(300)
bendera.pendown()

bendera.color("black","blue")
bendera.forward(100)
bendera.left(45)
bendera.forward(150)
bendera.left(45)
bendera.end_fill()
turtle.done()