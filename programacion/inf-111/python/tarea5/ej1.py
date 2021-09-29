import turtle 

turtle.pensize(2)  
turtle.bgcolor("black") 

colors = ["blue","yellow","red","green"] 

for i in range(120):        
    turtle.pencolor(colors[i % 4]) 
    turtle.fd(i+(i*2))   
    turtle.left(90)    

turtle.hideturtle()   
turtle.done()
