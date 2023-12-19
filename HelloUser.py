#  File: HelloUser.py
#  Author: Ahmed Hussein
#  Date: 09/11/2023
#  Description: A program that takes input of the user's name then greets the user.

#  Input/Output :
    # Input: a name.
    # Process: greet the user.
    # Output: a greeting message.

#  Pseudocode:
    # 1. Get the name of the user
    # 2. print out a greeting message.

# a function that takes in a name then prints out "t "Hello USER! My name is Ahmed.
def Hello(user):
    print("Hello " + user + "! " + "My name is Ahmed")

# Get the name of the user then store it in the user variable
user = input("Name: ") 
# supply the user variable to the Hello function.
Hello(user)

#  wait for input from the user to close the program
input("Press enter to close the program")