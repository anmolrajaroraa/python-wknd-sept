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

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
          'cyan', 'turquoise']

index = 0

print(len(colors))

'''for i in range(100):
    fred.color(colors[index])
    fred.circle(5 * i)
    fred.left(10)
    index += 1  #assignment shorthand    index = index + 1
    #print(index)
    if index == len(colors):
        index = 0
    print(index)

fred.dot(200)'''

for i in range(100):
    color = random.choice(colors)
    print(color)
    fred.color(color)
    fred.circle(5 * i)
    fred.left(10)

'''for i in range(25):
    for j in range(3):
        fred.forward(15 * i)
        fred.left(120)
    fred.backward(7.5)
    fred.right(90)
    fred.forward(5)
    fred.left(90)'''
