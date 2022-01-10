from turtle import Turtle, mainloop

tr = Turtle()
for j in range(200, 0, -10):
    tr.forward(j)
    tr.left(90)

mainloop()