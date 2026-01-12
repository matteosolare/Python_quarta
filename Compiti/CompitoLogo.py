##chiedo all'utente un numero positivo > 2 e disegnare il poligono a nLati

import turtle

n = int(input("Di quanti lati vuoi il poligono? -> "))
for i in range(n):
    turtle.forward(100)
    turtle.left(360 / n)
turtle.mainloop()