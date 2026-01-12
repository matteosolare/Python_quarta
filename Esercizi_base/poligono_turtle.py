import turtle

def sposta(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def poligono(n, lung):
    angolo = 360 / n
    for _ in range(n): # _ = i
        turtle.forward(lung)
        turtle.left(angolo)

def main():
    npoligoni = 4
    lato = 90
    shift = 180
    x_0, y_0 = -350, -lato/2
    for i in range(npoligoni):
        y = y_0
        x = x_0 + shift*i
        sposta(x, y)
        poligono(i+3, lato)
    turtle.mainloop()

if __name__ == "__main__":
    main()