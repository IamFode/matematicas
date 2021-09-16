import turtle

# crear lienzo
v=turtle.Screen()

#nubes
def nubes(x,y,radio,grado=180):
    n=turtle.Turtle()
    n.up()
    n.goto(x,y)
    n.down()
    n.circle(radio,grado)
    n.right(90)
    n.circle(radio,grado)
    n.right(180)
    n.circle(radio,grado)
    n.right(90)
    n.circle(radio,grado)
    n.right(90)
    n.circle(radio,grado)
    n.right(180)
    n.circle(radio,grado)
    n.hideturtle()
    n.up()

# nube grande
nubes(-100,-30,30)

# nube mediana 
nubes(200,0,20)

# nube pequeña
nubes(30,-20,10)




# Cierre la ventana con un clic
v.exitonclick()

