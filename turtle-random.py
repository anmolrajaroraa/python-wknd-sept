import turtle
import random

s = turtle.Screen()
s.bgcolor('black')
fred = turtle.Pen()
fred.shape('turtle')
fred.turtlesize(2,2)
fred.width(4)
fred.color('white')
fred.speed(0)
coordinates = list(range(-250,251))

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
          'cyan', 'turquoise']

shapes = ['square', 'triangle', 'circle', 'dot', 'octagon']

for i in range(50):
    #random color
    #random position
    #random shape
    fred.color(random.choice(colors))
    x = random.choice(coordinates)
    y = random.choice(coordinates)
    fred.penup()
    fred.setposition(x,y)
    fred.pendown()
    shape = random.choice(shapes)
    if shape == 'square':
        for i in range(4):
            fred.forward(100)
            fred.left(90)
    if shape == 'circle':
        fred.circle(50)   #radius
    if shape == 'triangle':
        for i in range(3):
            fred.forward(100)
            fred.left(120)
    if shape == 'dot':
        fred.dot(100)   #diameter
    if shape == 'octagon':
        for i in range(8):
            fred.forward(100)
            fred.left(45)
