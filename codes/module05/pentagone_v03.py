from turtle import Turtle, mainloop

nc = int(input("Nombre de cotés (>=3) ? "))
lc = int(input("Longueur d'un coté ? "))
tr = Turtle()

for i in range(nc):
    tr.forward(lc)
    tr.left(360 / nc)

mainloop()