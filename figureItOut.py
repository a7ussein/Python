#  File: figureItOut.py
#  Author: Ahmed Hussein
#  Date: 10/23/2023
#  Description: This program prompts the user to enter a number between 1 and 10 and depending on which number the user inputs a closed figure with sides the correspond to the inputted number 

#  Input/Output:
    #Input: a number of sides
    #Process: takes the number and based on it, prints a shape
    #Output: a shape.
    
#  Pseudocode:
    #1. configure points for each shape and store them in a variable that correspondes to the shape's name.
    #2. Define a function named drawShapes() which takes in a shapeNumber as input
    #3. use conditional statements to draw the shape based on the shapeNumber

from graphics import *

# Points for all shapes -- I used chatGpt to generate the points but most of them were random points that I just put in
point = Point(200, 200)
line = Line(Point(50, 200), Point(350, 200))
triangle = Polygon(Point(150, 133), Point(50, 233), Point(250,233))
square = Rectangle(Point(50, 50), Point(150, 150))
pentagon = Polygon(Point(200, 100), Point(138,172), Point(163, 272), Point(238, 272), Point(263,172))
hexagon = Polygon(Point(200, 100), Point(143, 165.36), Point(143, 234.64), Point(200, 300), Point(257, 234.64), Point(257, 165.36))
heptagon = Polygon(Point(200, 100), Point(157.79, 157.79), Point(100, 200), Point(157.79, 242.21), Point(200, 300), Point(242.21, 242.21), Point(300, 200))
octagon = Polygon(Point(200, 70.71), Point(141.42, 141.42), Point(70.71, 200), Point(141.42, 258.58), Point(200, 329.29), Point(258.58, 258.58), Point(329.29, 200), Point(258.58, 141.42))
nonagon = Polygon(Point(200, 100), Point(157.79, 142.21), Point(114.28, 185.92), Point(85.71, 242.21), Point(100, 300), Point(157.79, 342.21), Point(214.28, 385.92), Point(242.85, 342.21), Point(257.15, 284.92))
decagon = Polygon(Point(200, 100), Point(242.64, 128.21), Point(257.36, 171.79), Point(242.64, 214.28), Point(200, 242.64), Point(157.36, 214.28), Point(142.64, 171.79), Point(128.21, 128.21), Point(142.64, 85.72), Point(200, 100))

# A function that takes in the number of sides and draws the shape
def drawShapes(shapeNumber):
    win = GraphWin("FigureItOut", 400, 400)
    
    if shapeNumber == 1:
        point.draw(win)
    elif shapeNumber == 2:
        line.draw(win)
    elif shapeNumber == 3:
        triangle.draw(win)
    elif shapeNumber == 4:
        square.draw(win)
    elif shapeNumber == 5 :
        pentagon.draw(win)
    elif shapeNumber == 6:
        hexagon.draw(win)
    elif shapeNumber == 7 :
        heptagon.draw(win)
    elif shapeNumber ==8 :
        octagon.draw(win)
    elif shapeNumber == 9 :
        nonagon.draw(win)
    elif shapeNumber == 10 :
        decagon.draw(win)

# wait for the user to click on the mouse then close the window
    win.getMouse()
    win.close()

# I had to define a main function because other wise the window would be drawn before the user inputs a number in terminal
def main():
    getNumber = input("Input a number between 1 and 10: ")
    drawShapes(int(getNumber))

main()