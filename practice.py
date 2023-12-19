from graphics import *

win = GraphWin("shapes")

center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill("red")
circ.draw(win)

label = Text(center, "Red Circle")
label.draw(win)

rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)

line = Line(Point(20, 30), Point(70,70))
line.draw(win)
input() 