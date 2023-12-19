#  File: RYB.py
#  Author: Ahmed Hussein
#  Date: 09/21/2023
#  Description: This program is going to use the RYB subtractive color model


#  Input/Output:
    #Input: Two primary colors
    #Process: check what the input was and if it is not one of the allowed colors output an error else print out the combination of the two colors
    #Output: the combination of the two inputted colors
    
#  Pseudocode: 
    #1. Initialize a list with the colors that are allowed to be inputted
    #2. Get the first color from the user
    #3. Get the second color from the user
    #4. Check if the inputted colors are in the list of allowed colors
    #5. If the inputted colors are not in the list of allowed colors output an error
    #6. If the inputted colors are in the list of allowed colors check what the combination of the two colors is and output the result
    #7. If the inputted colors are the same output an error

# list of allowed colors
listOfPrimaryColors = ["Red", "red", "Yellow", "yellow", "Blue", "blue"]

# Get the first color from the user
color1 = input("Enter a primary color (Red, Yellow, Blue): ")
# Get the second color from the user
color2 = input("Enter another primary color (Red, Yellow, Blue): ")

# list of the colors and their combinations based on the RYB modle
# yellow + blue = Green
# yellow + red = Orange

# red + yellow = Orange
# red + blue = Purple

# blue + yellow = Green
# blue + red = Purple

# Check if the inputted colors are not in the list
if color1 not in listOfPrimaryColors or color2 not in listOfPrimaryColors:
    print("Error, you did not enter a primary color")
else:
    # Check various combinations of primary colors and print the result. 
    if color1 == "Yellow" and color2 == "Blue" or color1 == "yellow" and color2 == "blue":
        print(str(color1) + " + " + str(color2) + " = " + "Green")
    elif color1 == "Blue" and color2 == "Yellow" or color1 == "blue" and color2 == "yellow":
        print(str(color1) + " + " + str(color2) + " = " + "Green")
    elif color1 == "Yellow" and color2 == "Red" or color1 == "yellow" and color2 == "red" :
        print(str(color1) + " + " + str(color2) + " = " + "Orange")
    elif color1 == "Red" and color2 == "Yellow" or color1 =="red" and color2 == "yellow" :
        print(str(color1) + " + " + str(color2) + " = " + "Orange")
    elif color1 == "Red" and color2 == "Yellow" or color1 == "red" and color2 == "yellow":
        print(str(color1) + " + " + str(color2) + " = " + "Orange")
    elif color1 == "Yellow" and color2 == "Red" or color1 == "yellow" and color2 =="red":
        print(str(color1) + " + " + str(color2) + " = " + "Orange")
    elif color1 == "Red" and color2 == "Blue" or color1 == "red" and color2 == "blue":
        print(str(color1) + " + " + str(color2) + " = " + "Purple")
    elif color1 == "Blue" and color2 == "Red" or color1 == "blue" and color2 == "red":
        print(str(color1) + " + " + str(color2) + " = " + "Purple")
    elif color1 == "Blue" and color2 == "Yellow" or color1 == "blue" and color2 == "yellow":
        print(str(color1) + " + " + str(color2) + " = " + "Green")
    elif color1 == "Yellow" and color2 == "Blue" or color1 == "yellow" and color2 == "blue":
        print(str(color1) + " + " + str(color2) + " = " + "Green")
    elif color1 == "Blue" and color2 == "Red" or color1 == "blue" and color2 == "red":
        print(str(color1) + " + " + str(color2) + " = " + "Purple")
    elif color1 == "Red" and color2 == "Blue" or color1 == "reed" and color2 == "Blue":
        print(str(color1) + " + " + str(color2) + " = " + "Purple")
    else:
        print("You entered the same color twice")