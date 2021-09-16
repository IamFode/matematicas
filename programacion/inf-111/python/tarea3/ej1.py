import turtle

# Crea la ventana
v=turtle.Screen()

# Crea la tortuga azul
azul=turtle.Turtle()
# Dibujar circulo azul 
azul.up()
azul.forward(-150)
azul.right(50)
azul.down()
azul.color("blue")
azul.pensize(5)
azul.circle(50)
azul.hideturtle()


# Crea la tortuga negro 
negro=turtle.Turtle()
# Dibujar circulo negro 
negro.up()
negro.forward(-40)
negro.right(50)
negro.down()
negro.color("black")
negro.pensize(5)
negro.circle(50)
negro.hideturtle()


# Crea la tortuga rojo 
rojo=turtle.Turtle()
# Dibujar circulo rojo 
rojo.up()
rojo.forward(70)
rojo.right(50)
rojo.down()
rojo.color("red")
rojo.pensize(5)
rojo.circle(50)
rojo.hideturtle()


# Crea la tortuga amarillo 
amarillo=turtle.Turtle()
# Dibujar circulo amarillo 
amarillo.up()
amarillo.forward(-10)
amarillo.left(120)
amarillo.down()
amarillo.color("yellow")
amarillo.pensize(5)
amarillo.circle(50)
amarillo.hideturtle()


# Crea la tortuga verde 
verde=turtle.Turtle()
# Dibujar circulo verde 
verde.up()
verde.forward(100)
verde.left(120)
verde.down()
verde.color("green")
verde.pensize(5)
verde.circle(50)
verde.hideturtle()


# Cierre la ventana con un clic
v.exitonclick()

