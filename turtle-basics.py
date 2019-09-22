Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> s = turtle.Screen()
>>> s.bgcolor('black')
>>> t = turtle.Pen()
>>> t.color('white')
>>> t.turtlesize(2,2)
>>> t.shape('turtle')
>>> #screen size is 700px by 700px
>>> t.forward(300)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.width(4) #size for line drawn
>>> t.forward(300)
>>> t.left(90)
>>> t.forward(100)
>>> t.color('yellow')
>>> t.left(90)
>>> t.forward(300)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(300)
>>> t.left(90)
>>> t.forward(100)
>>> t.dot(50)
>>> s.resetscreen()
>>> t.reset()
>>> t.color('white')
>>> t.turtlesize(2,2)
>>> t.color('yellow')
>>> t.fillcolor('yellow')
>>> t.begin_fill
<bound method RawTurtle.begin_fill of <turtle.Turtle object at 0x108c05908>>
>>> t.begin_fill()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.end_fill()
>>> t.color('blue')
>>> t.write("Square", True, font = "Arial", 16, "normal")
SyntaxError: positional argument follows keyword argument
>>> t.write("Square", True, font=("Arial", 16, "normal"))
>>> t.hideturtle()
>>> t.showturtle()
>>> t.write("Square", False, font=("Arial", 16, "normal"))
>>> t.hideturtle()
>>> t.showturtle()
>>> t.forward(100)
>>> t.color('yellow')
>>> t.penup()
>>> t.forward(50)
>>> t.write("Square", True, font=("Arial", 16, "normal"))
>>> t.hideturtle()
>>> t.showturtle()
>>> t.left(90)
>>> t.forward(100)
>>> t.pendown()
>>> t.forward(100)
>>> t.reset()
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for x in [0,1,2,3]:
	print(x)

0
1
2
3
>>> for x in range(4):
	print(x)

	
0
1
2
3
>>> turtle.color('yellow')
>>> turtle.shape('turtle')
>>> for x in range(4):
	t.forward(100)
	t.left(90)

	
>>> turtle.color('yellow')
>>> t.pendown()
>>> for x in range(4):
	turtle.forward(100)
	turtle.left(90)

	
>>> 
