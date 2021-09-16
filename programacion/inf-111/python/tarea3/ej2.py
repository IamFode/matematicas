import turtle

# Crea la ventana
v=turtle.Screen()
#color de fondo
v.bgcolor("blue")
# dimensión de pantalla
turtle.screensize(500,500)

# dibujar la letra C
c=turtle.Turtle()
c.pensize(20)
c.color("white")
c.up()
c.goto(-50,120)
c.down()
c.bk(130)
c.right(90)
c.fd(200)
c.left(90)
c.fd(130)

# dibujar la letra P
p=turtle.Turtle()
p.pensize(20)
p.color("white")
p.up()
p.goto(50,120)
p.down()
p.rt(90)
p.fd(200)
p.up()
p.setx(50)
p.sety(0)
p.down()
p.lt(50)
p.circle(77,260)

# Cierre la ventana con un clic
v.exitonclick()


