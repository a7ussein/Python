#  File: gpa.py
#  Author: Ahmed Hussein
#  Date: 09/19/2023
#  Description: a program to calculate the gpa based on the number of quality points and the nubmer of credits attempt


#  Input/Output:
    #Input: number of quality points and number of credits attempt
    #Process: divide the number of quality points by the total number of credits attempt
    #Output: the gpa
    
#  Pseudocode: 
    #1. Get the total number of quality points from the user
    #2. Get the total number of credits attempt from the user
    #3. divide the total number of quality points by the total number of credits attempt
    #4. print the GPA as a numeric value
    #5. print the GPA as a letter grade
    
    
# Get the number of quality points from the user
qualityPoints = eval(input("Enter the number of quality points: "))
# Get the total number of credits attempt from the user
creditsAttempt = eval(input("Enter the total number of credits attempt: "))
# divide the total number of quality points by the total number of credits attempt
gpa = qualityPoints/creditsAttempt

# Check if GPA is less than 0 or greater than 4.0
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