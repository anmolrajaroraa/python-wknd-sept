import turtle
s = turtle.Screen()
s.bgcolor('black')
fred = turtle.Pen()
fred.shape('turtle')
fred.turtlesize(2,2)
fred.width(4)


fred.color('blue')
fred.fillcolor('blue')
fred.begin_fill()
for i in range(4):
    fred.forward(100)
    fred.left(90)
fred.end_fill()
fred.color('yellow')
fred.write("Square", font=("Arial", 25, 'bold'))
fred.penup()
fred.setposition(0,-200)
fred.pendown()
fred.fillcolor('yellow')
fred.begin_fill()
for i in range(4):
    fred.forward(100)
    fred.left(90)
fred.end_fill()
fred.color('blue')
fred.write("Square", font=("Arial", 25, 'bold'))
