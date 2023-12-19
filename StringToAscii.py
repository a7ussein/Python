#  File: StringToAscii.py
#  Author: Ahmed Hussein
#  Date: 09/11/2023
#  Description: This program aims to convert a string into ascii characters
#  Citation: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

#  Input/Output :
    # Input: a string
    # Process: convert the input into ascii characters
    # Output: a list of ascii characters

#  Pseudocode:
    # 1. Get the string from the user
    # 2. split the string into a list of characters
    # 3. loop through the string and store them into a list
    # 4. print the list of ascii characters.


# a function that takes in a string then prints out the ascii characters of the string.
def convert(string):
    # split the string into a list of characters
    string = list(string)
    # loop through the string and store them into a list
    convertion = []
    for i in string:
       char = ord(i)
       convertion.append(char)
    # print the list of ascii characters.
    print(convertion)

string = input("String: ")

convert(string)

#  wait for input from the user to close the program
input("Press enter to close the program")