# libraría 
import turtle

# variable de entrada
dibujo = input("¿Qué figura quiere dibujar?: ")

# triangulo
if dibujo == "t":

    v=turtle.Screen()
    t=turtle.Turtle()
    t.fillcolor("red")
    t.begin_fill()
    t.color("red")
    t.left(110)
    t.fd(100)
    t.left(140)
    t.fd(100)
    t.left(110)
    t.fd(65)
    t.hideturtle()
    t.end_fill()
    v.exitonclick()

# cuadrado
elif dibujo == "r":

    v=turtle.Screen()
    r=turtle.Turtle()
    r.fillcolor("blue")
    r.begin_fill()
    r.up()
    r.goto(-50,0)
    r.down()
    r.fd(150)
    r.left(90)
    r.fd(100)
    r.left(90)
    r.fd(150)
    r.left(90)
    r.fd(100)
    r.hideturtle()
    r.end_fill()
    v.exitonclick()

# circulo
elif dibujo == "c":

    v=turtle.Screen()
    r=turtle.Turtle()
    r.fillcolor("yellow")
    r.begin_fill()
    r.circle(70)
    r.hideturtle()
    r.end_fill()
    v.exitonclick()

else:
    print("Letra no válida")
