from turtle import Turtle, mainloop
tr = Turtle()
# Dessiner un carré
for i in range(4):
    tr.forward(20)
    tr.left(90)
tr.penup()
tr.forward(25)
tr.pendown()
# Dessiner un triangle
for i in range(3):
    tr.forward(20)
    tr.left(120)
tr.penup()
tr.forward(25)
tr.pendown()
mainloop()