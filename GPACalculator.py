# File: GPACalculator.py
# Author: Ahmed Hussein
# Date: 12/11/2023
# Description: A program to calculate GPA

# Input/Output:
    # Input: Number of classes, Course information (number, name, letter grade, credit hours)
    # Process: Calculate GPA, Validate input, Display semester GPA and corresponding letter grade
    # Output: Semester GPA and Letter Grade

# Pseudocode:
    # 1. Take in the total number of classes
    # 2. Initialize total quality points and total credit hours to zero
    # 3. Loop through each class to input course information
        # a. Get course number, course name, letter grade, and credit hours
        # b. Calculate quality points based on the letter grade
        # c. Update total quality points and total credit hours
    # 4. Calculate semester GPA using total quality points and total credit hours
    # 5. Display semester GPA and corresponding letter grade
    # 6. If GPA is out of range, display an error message
    
# function to calculate the GPA based on the provided letter grade.
def calculateGPA(letterGrade):
    gradePoints = {'A': 4.00, 'A-': 3.67, 'B+': 3.33,
                   'B': 3.00, 'B-': 2.67, 'C+': 2.33,
                   'C': 2.00, 'C-': 1.67, 'D+': 1.33,
                   'D': 1.00, 'F': 0.00}
    return gradePoints.get(letterGrade, 0.00)

# Function to calculate the semesterGPA
def calculateSemesterGPA(qualityPoints, credits):
    if credits == 0:
        return 0.00
    return qualityPoints / credits

# Function to convert semester GPA to corresponding letter grade.

def semesterGPALetterConverter(semester_gpa):
    if semester_gpa >= 3.67:
        return "A"
    elif semester_gpa >= 3.33:
        return "A-"
    elif semester_gpa >= 3.00:
        return "B+"
    elif semester_gpa >= 2.67:
        return "B"
    elif semester_gpa >= 2.33:
        return "B-"
    elif semester_gpa >= 2.00:
        return "C+"
    elif semester_gpa >= 1.67:
        return "C"
    elif semester_gpa >= 1.33:
        return "C-"
    elif semester_gpa >= 1.00:
        return "D+"
    elif semester_gpa >= 0.00:
        return "D"
    else:
        return "F"

# main function to put everything together
def main():
    totalGPA = 0
    totalCredits = 0
    
    classes = int(input("Enter the total number of classes you took: "))
    for i in range(classes):
        print("Enter information for class #" + str(i + 1))
        courseNumber = input("Enter course number: ")
        courseName = input("Enter course name: ")
        letterGrade = input("Enter letter grade: ")
        credits = float(input("Enter credit hours: "))
        print("\n")
        GPA = calculateGPA(letterGrade)
        totalGPA += GPA * credits
        totalCredits += credits
    
    semesterGPA = calculateSemesterGPA(totalGPA, totalCredits)
    if semesterGPA < 0.00 or semesterGPA > 4.00:
        print("GPA out of range.")
    else:
        print("Semester GPA:", "{:.2f}".format(semesterGPA))
        print("Letter Grade:", semesterGPALetterConverter(semesterGPA))

if __name__ == "__main__":
    main()
