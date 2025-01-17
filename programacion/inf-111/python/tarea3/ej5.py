import turtle

# crear lienzo
v=turtle.Screen()
v.bgcolor("#A8EBE1")

# nubes 
def nubes(x,y,radio,grado=180):
    nube=turtle.Turtle()
    nube.fillcolor("#A8EBE1")
    nube.color("white")
    nube.begin_fill()
    nube.up()
    nube.goto(x,y)
    nube.down()
    nube.circle(radio,grado)
    nube.right(90)
    nube.circle(radio,grado)
    nube.right(180)
    nube.circle(radio,grado)
    nube.right(90)
    nube.circle(radio,grado)
    nube.right(90)
    nube.circle(radio,grado)
    nube.right(180)
    nube.circle(radio,grado)
    nube.hideturtle()
    nube.up()
    nube.end_fill()

# nube grande
nubes(-140,170,15)

# nube mediana 
nubes(200,150,10)

# nube pequeña
nubes(20,150,5)
nubes(130,190,5)

# Sol
sol = turtle.Turtle()
sol.color("yellow")
sol.up()
sol.goto(-40,170)
sol.down()
sol.fillcolor("yellow")
sol.begin_fill()
sol.circle(20)
sol.hideturtle()
sol.end_fill()

# Montañas
mont=turtle.Turtle()
mont.fillcolor("brown")
mont.color("brown")
mont.up()
mont.goto(-350,-40)
mont.down()
mont.begin_fill()
mont.left(45)
mont.fd(150)
mont.right(90)
mont.fd(150)
mont.left(90)
mont.fd(250)
mont.right(90)
mont.fd(250)
mont.left(90)
mont.fd(83)
mont.right(83)
mont.fd(90)
mont.hideturtle()
mont.end_fill()
mont.hideturtle()

# pasto
pasto=turtle.Turtle()
pasto.up()
pasto.fillcolor("#7AF268")
pasto.color("#7AF268")
pasto.goto(-340,-40)
pasto.down()
pasto.begin_fill()
pasto.right(90)
pasto.fd(250)
pasto.left(142)
pasto.fd(318)
pasto.end_fill()
pasto.up()
pasto.home()
pasto.fillcolor("#7AF268")
pasto.color("#7AF268")
pasto.goto(340,-40)
pasto.down()
pasto.begin_fill()
pasto.right(90)
pasto.fd(250)
pasto.right(90)
pasto.fd(570)
pasto.right(110)
pasto.fd(268)
pasto.end_fill()
pasto.hideturtle()

# arboles
def arbol(x,y,radio,grado=180):
    arbol=turtle.Turtle()
    arbol.fillcolor("#418037")
    arbol.color("#418037")
    arbol.up()
    arbol.goto(x,y)
    arbol.down()
    arbol.begin_fill()
    arbol.circle(radio,grado)
    arbol.right(160)
    arbol.circle(3*radio/4,grado)
    arbol.right(170)
    arbol.circle(2*radio/3,grado)
    arbol.right(60)
    arbol.circle(2*radio/3,grado)
    arbol.right(170)
    arbol.circle(3*radio/4,grado)
    arbol.right(160)
    arbol.circle(radio,grado)
    arbol.hideturtle()
    arbol.end_fill()
    t=turtle.Turtle()
    t.up()
    t.goto(x-radio,y)
    t.color("brown")
    t.pensize(radio)
    t.down()
    t.right(90)
    t.fd(radio)
    t.hideturtle()

arbol(300,-240,40)
arbol(0,-45,5)
arbol(19,-46,7)
arbol(39,-45,6)
arbol(56,-45,9)

# carro
car = turtle.Turtle()
car.color('blue')
car.fillcolor('blue')
car.penup()
car.goto(-50,-140)
car.pendown()
car.begin_fill()
car.forward(100)
car.left(90)
car.forward(20)
car.left(90)
car.forward(100)
car.left(90)
car.forward(20)
car.end_fill()
car.penup()
car.goto(-48,-140)
car.pendown()
car.setheading(45)
car.forward(50)
car.setheading(0)
car.forward(20)
car.setheading(-45)
car.forward(20)
car.setheading(90)
car.penup()
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.up()
car.goto(40,-140)
car.circle(7)
car.end_fill()
car.penup()
car.goto(-28, -140)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(7)
car.end_fill()
    
car.hideturtle()

# Cierre la ventana con un clic
v.exitonclick()

