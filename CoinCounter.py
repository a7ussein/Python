#  File: CoinCounter.py
#  Author: Ahmed Hussein
#  Date: 09/11/2023
#  Description: The program is going to prompt the user for how many pennies, nickles, dimes and quarters the user has.
#  Then, it would tell the user the total monetary value of their coins. 

#  Input/Output:
    #Input: number of quarters, dimes, nickels, pennies that users have.
    #Process: convert the number of quarters, dimes, nickels, pennies into their coin value.
    #Output: the total value of the coins.
    
#  Pseudocode:
    #1. Get the number of quarters, dimes, nickels, pennies from the user.
    #2. convert the quarters, dimes, nickels, pennies into their coin value.
    #3. print the total value of the coins.


# a function that converts the quarters, dimes, nickels, pennies into their coin value
def convert(quarters, dimes, nickels, pennies):
    coins = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print("The total value of your change is $" + str(coins))

# Get the number of quarters, dimes, nickels, pennies from the user.
quarters = eval(input("Quarters: "))
dimes = eval(input("Dimes: "))
nickels = eval(input("Nickels: "))
pennies = eval(input("Pennies: "))

convert(quarters, dimes, nickels, pennies)

#  wait for input from the user to close the program
input("Press enter to close the program")