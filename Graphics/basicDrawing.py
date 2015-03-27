from graphics import *

datafile = open("data.txt")
pureData = datafile.readlines()

data = []

for num in pureData:
    data.append(float(num))
    
win = GraphWin("Data Visualisation", 1000, 300)

lastRadius = 0

for number in data:
    ball = Circle(Point(lastRadius,100), number/2)
    ball.setFill(color_rgb(255,255,0))
    ball.draw(win)
    lastRadius = lastRadius + (number * 2)

win.getMouse()