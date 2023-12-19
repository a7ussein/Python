#  File: gpa.py
#  Author: Ahmed Hussein
#  Date: 10/16/2023
#  Description: The program takes in a numerical grade and converts it to its corresponding Letter grade

#  Input/Output:
    #Input: A numerical grade
    #Process: Converts that numerical grade into a letter grade
    #Output: prints out the letter grade
    
    
#  Pseudocode:
    #1. Get the numerical grade from the user.
    #2. Create a function that takes in the grade and based on how much it is, the function returns the corresponding letter to the grade
    #3. Print the letter that corresponds to the numerical grade.

# get the numerical grade from the user 
grade = float(input("Enter your numeric grade: "))

# function to convert the numerical grade to a letter. 
def convertGradeToLetter(grade):
    if grade >= 95:
        return "A"
    elif grade >= 93:
        return "A-"
    elif grade >=91:
        return "B+"
    elif grade >= 87:
        return "B"
    elif grade >= 85:
        return "B-"
    elif grade >= 83:
        return "C+"
    elif grade >= 79:
        return "C"
    elif grade >= 77:
        return "C-"
    elif grade >= 75:
        return "D+"
    elif grade >= 70:
        return "D"
    else:
        return "F"

# print the letter grade
print("Your letter grade is:", convertGradeToLetter(grade))

#  wait for input from the user to close the program
input("Press enter to close the program")