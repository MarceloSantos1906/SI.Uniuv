'''
Bandeira do Brasil com turtle ultilizando python conforme conversei como o professor em sala de aula
Por: Marcelo dos Santos Junior

'''

import turtle

turtle.speed(3)
turtle.pensize(2)

turtle.color("green")
turtle.begin_fill()
turtle.forward(350)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(350)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.end_fill()

turtle.color("black")
turtle.penup()
turtle.goto(0,0)

turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(90)
turtle.right(180)

turtle.color("yellow")
turtle.right(140)
turtle.pendown()
turtle.begin_fill()
turtle.forward(120)
turtle.right(80)
turtle.forward(120)
turtle.right(100)
turtle.forward(120)
turtle.right(80)
turtle.forward(120)
turtle.end_fill()

turtle.right(140)

turtle.penup()
turtle.color("blue")
turtle.goto(0,0)
turtle.forward(142)
turtle.right(90)
turtle.forward(100)

turtle.pendown()
turtle.begin_fill()
turtle.circle(40)
turtle.penup()
turtle.end_fill()

turtle.color("white")
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.backward(20)
turtle.left(90)
turtle.forward(8)
turtle.right(45)

turtle.pendown()
turtle.pensize(10)
turtle.circle(110,39)

turtle.hideturtle()

turtle.getscreen()._root.mainloop() 