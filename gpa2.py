qualityPoints = eval(input("Enter quality points: "))
creditsAttempt = eval(input("Enter total credits attempted: "))

def gpaCalc(qualityPoints, creditsAttempt):
    gpa = qualityPoints/creditsAttempt

    if gpa < 0.0 or gpa > 4.0:
        print("Error")
    else:
        # Determine the letter grade based on GPA ranges
        if gpa >= 3.68 and gpa < 4.00:
            print("A")
        elif gpa >= 3.34 and gpa < 3.68:
            print("A-")
        elif gpa >= 3.01 and gpa < 3.34:
            print("B+")
        elif gpa >= 2.68 and gpa < 3.00:
            print("B-")
        elif gpa >= 2.01 and gpa < 2.33:
            print("C+")
        elif gpa >= 1.68 and gpa < 2.00:
            print("C-")
        elif gpa >= 1.01 and gpa < 1.33:
            print("D+")
        elif gpa >= 0.68 and gpa < 1.00:
            print("D")
        else:
            print("F")

gpaCalc(qualityPoints, creditsAttempt)