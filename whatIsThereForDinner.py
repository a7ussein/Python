#  File: WhatIsThereForDinner.py
#  Author: Ahmed Hussein
#  Date: 11/30/2023
#  Description: The program determines what is there for dinner based on the available ingredients

#  Input/Output:
    #Input: number of ingredients the user has and the ingredients
    #Process: stores the ingredients in an array then determines which options are available for dinner based on the available ingredients
    #Output: prints out the available options
    
    
#  Pseudocode:
    #1. Get the number of ingredients from the user
    #2. based on the provided number ask the user for each ingredient then store it in a list
    #3. create nested if statements to determine which ingredients are available and based on that print out the available options
    
# get the number of ingredients from the user
numberOfIngredients = int(input("How many ingredients do you have: "))
ingredients = []

# ask the user for ingredients then store them in a list
for i in range(0, numberOfIngredients):
    ingredientName = input("Enter the name of ingredient number " + str(i+1) + ": ")
    ingredients.append(ingredientName.lower())

# if stements to determine which ingredients match with which available options. 
if "eggs" in ingredients:
    print("Eggs is available for dinner")
    if "beef" in ingredients:
        print("Steak and Eggs are available for dinner")
        if "cheese" in ingredients:
            print("Frittata is available for dinner")
        else:
            print("Steak and Eggs are available for dinner")
    else:
        print("Omlet is available for dinner")
elif "beef" in ingredients:
    if "cheese" in ingredients:
        print("Cheese Burger is available for dinner")
    else:
        print("Steak is available for dinner")
elif "cheese" in ingredients:
    print("Toasted Cheese is available for dinner")
else:
    print("No meal option found with these ingredients.")
