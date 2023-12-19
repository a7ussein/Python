#  File: factorial.py
#  Author: Ahmed Hussein
#  Date: 09/19/2023
#  Description: A program that takes in a whole number and lis


#  Input/Output:
    #Input: 
    #Process: 
    #Output: 
    
#  Pseudocode: 
    # 1. get a whole number from the user. 
    # 2. find its factorials and multiply them by each other

wholeNumber = int(input("Please enter a whole number: "))


def findFactorial(wholeNumber):
    fact = 1
    for num in range(wholeNumber, 1, -1):
        fact = fact * num
        print(str(num) + " *", end = ' ')
    print("1 =", fact)

findFactorial(wholeNumber)