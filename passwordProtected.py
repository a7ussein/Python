#  File: passwordProtected.py
#  Author: Ahmed Hussein
#  Date: 10/23/2023
#  Description: A program that takes in a password from the user and checks if matches the cariteria of a secure password

#  Input/Output:
    #Input: a password
    #Process: checks if the password matches the cariteria of a secure password
    #Output: if the password is valid or not
    
#  Pseudocode:
    #1. Prompt the user for a password
    #2. create booleans for the cariteria and set them as false and make them true as conditions get checked
    #3. use conditional statements to see if the password matches the carteira and change the booleans from false to true or keep them as false if it doesn't match

# ask the user for password
password = input("Input your password: ")

# booleans for cariteria
Length = False
uppercase = False
lowercase = False
number = False
special_characters = False
# list of special characters
SpecialCharacters = '[@_!#$%^&*()<>?/\|}{~:]' #Got this from geeksforgeeks.org 

# check the length of the password and if it is more than or equal to 12 change the Length boolean to true
if len(password) >= 12:
    Length = True
else:
    Length = False

# Check the rest of the conditions based on each character in the password
for char in password:
    if (ord(char) >= 65 and ord(char) <= 90):  # ASCII value of A-Z
        uppercase = True
    elif (ord(char) >= 97 and ord(char) <= 122):  # ASCII value of a-z
        lowercase = True
    elif (ord(char) >= 48 and ord(char) <= 57):  # ASCII value of 0-9
        number = True
    elif char in SpecialCharacters:
        special_characters = True

# if all the caritera are true, print password is valid otherwaise print password is invalid. 
if(Length and uppercase and lowercase and number and special_characters):
    print("Password is valid")
else:
    print("Password is invalid :(")