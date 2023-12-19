from graphics import *

def draw_shapes(shape_number):
    win = GraphWin("FigureItOut", 400, 400)

    if shape_number == 1:
        point = Point(200, 200)
        point.draw(win)
    elif shape_number == 2:
        line = Line(Point(50, 200), Point(350, 200))
        line.draw(win)
    elif shape_number == 3:
        triangle = Polygon(Point(150, 133), Point(50, 266), Point(250, 266))
        triangle.draw(win)
    elif shape_number == 4:
        square = Rectangle(Point(100, 100), Point(300, 300))
        square.draw(win)
    elif shape_number == 5:
        pentagon = Polygon(Point(200, 100), Point(138, 172), Point(163, 272), Point(238, 272), Point(263, 172))
        pentagon.draw(win)
    elif shape_number == 6:
        hexagon = Polygon(Point(200, 100), Point(143, 165.36), Point(143, 234.64), Point(200, 300),
                          Point(257, 234.64), Point(257, 165.36))
        hexagon.draw(win)
    # Add more shapes as needed

    win.getMouse()
    win.close()

def main():
    getNumber = input("Input a number between 1 and 6: ")

    try:
        shape_number = int(getNumber)
        if 1 <= shape_number <= 6:
            draw_shapes(shape_number)
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()