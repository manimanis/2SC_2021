from turtle import Turtle, mainloop

tr = Turtle()

for i in range(7):
    for nc in range(4, 2, -1):
        for i in range(nc):
            tr.forward(20)
            tr.left(360 / nc)
        tr.penup()
        tr.forward(25)
        tr.pendown()

mainloop()