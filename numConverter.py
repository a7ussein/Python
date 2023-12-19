#  File: numConverter.py
#  Author: Ahmed Hussein
#  Date: 12/10/2023
#  Description: A program to take in two integer values - a number and a base then perform a series of operations on the number based on its base then output a string

#  Input/Output:
    #Input: A number and a base
    #Process: Validates the entered numbers then divide the number the number by the base and if the remainder is greater than 9, it is converted to a letter then concatenated to a string
    # and it coninues that process of dividing the number by the base until the result is less than or equal to 1 then it concatenate the final remainder to the string
    #Output: A reversed string
    
#  Pseudocode:
    #1. Take in two integers - a number and a base
    #2. Validate input and ensure that the base is not higher than 16
    #3. Divide the Number by the Base
    #4. If the reminder of the division is 0 then conctenate 0 to a string
    #5. If the reminder of the division is not 0 then check if it is larger than 9
    #6. If it is larger than 9 then convert it to a letter and concatenate it to the string. 
    #7. If it is not larger than 9 then continue the division by the base process while updating the value of the Number until it is less than or equal to 1
    #8. Concatenate the final reminder onto the string
    #9. Print the string in reverse

# Input
Number = int(input("Enter a number: "))
Base = int(input("Enter a base: "))

# Function to make sure that the base is never larger than 16
def checkBase():
    if Base > 16:
        print("Base is too high; max is 16")
        exit()
    else:
        return Base
# Function to convert numbers larger than 9 to letters
def convertToLetter(remainder):
    if remainder == 10:
        return "A"
    elif remainder == 11:
        return "B"
    elif remainder == 12:
        return "C"
    elif remainder == 13:
        return "D"
    elif remainder == 14:
        return "E"
    elif remainder == 15:
        return "F"
    else:
        return str(remainder)

# The function Process is basically the main function but I called it process cus it is more describtive : >
def process(Number, Base):
    Base = checkBase()
    string = ""
    
    # a loop to keep the devision process going as long as the Number is larger than 1
    while Number > 1:
        remainder = Number % Base
        print("number: ", Number, "remainder: ", remainder)
        if(remainder == 0):
            string += str(remainder)
        else:
            if(remainder > 9):
                string += convertToLetter(remainder)
        Number = Number//Base
        # I had to create this if statement because if the input was 255 and 16 the output used to be 0FF instead of FF
    if(Number == 1):
        string += str(Number)
    else:
        string = string
    print(string[::-1])

process(Number, Base)