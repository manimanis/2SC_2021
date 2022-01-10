from turtle import Turtle, mainloop

tr = Turtle()
tr.hideturtle()
tr.speed(0)

cote = 50
color = 'black'

for y in range(8):
    tr.penup()
    tr.setposition(-cote*4, cote*(y-4))
    tr.pendown()
    for x in range(8):
        if (x+y) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        tr.color('black', color)
        tr.begin_fill()
        for i in range(4):
            tr.forward(cote)
            tr.left(90)
        tr.end_fill()
        tr.penup()
        tr.forward(cote)
        tr.pendown()

mainloop()