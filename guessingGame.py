#  File: guessingGame.py
#  Author: Ahmed Hussein
#  Date: 12/4/2023
#  Description: This program is intended to be a game where the user guesses a number and the
# program figures it out based on a specific range that the user inputs for the number they guessed 

#  Input/Output:
    #Input: A range that contains the number in which the user is thinking about 
    #Process: The program prompts the user to think about a number in their head. Then prompts the user to enter a range that the number they are thinking of lays within
    # The program then uses the square root of that range 
    #Output: prints out the available options
    
    
# Pseudocode:
# 1. Prompt the user to think about a random number and press the enter key.
# 2. Get the starting and ending range values from the user.
# 3. Calculate the maximum number of guesses based on the square root of the range.
# 4. Initialize the guess count to 0.
# 5. Start a loop while the starting range is less than or equal to the ending range.
    # 6. Calculate the midpoint guess.
    # 7. Increment the guess count.
    # 8. Display the current guess number, the guess, and the number of guesses left.
    # 9. Ask the user if the guess is too high, too low, or correct.
    # 10. If the guess is too high, update the ending range.
    # 11. If the guess is too low, update the starting range.
    # 12. If the guess is correct, print "I win!" and exit the loop.
    # 13. If the user provides an invalid input, decrement the guess count.
# 14. Check if the user is cheating (ending range less than starting range).
    # 15. If cheating is detected, print a message indicating possible cheating.
# 16. If the loop is complete without a correct guess, print "You win!"

import math

print("-------- GUESSING GAME -------- ")
input("Think about a random number then press the enter key: ")
startingRange = int(input("Enter a starting range value: "))
endingRange = int(input("Enter an ending range: "))
maxGuesses = int(math.sqrt(endingRange - startingRange))
guessCount = 0  # Initialize the guess count

while startingRange <= endingRange:  # Ensure the ranges are valid

    guess = math.ceil((startingRange + endingRange) / 2)
    guessCount += 1  # Increment the guess count

    print("Guess number:", guessCount)
    print("My guess is", guess)
    print("Number of guesses left:", maxGuesses - guessCount)

    wasItCorrect = input("Was my guess too high, too low, or correct? ").lower()
    if wasItCorrect == "too high":
        endingRange = guess - 1
    elif wasItCorrect == "too low":
        startingRange = guess + 1
    elif wasItCorrect == "correct":
        print("I win!")
        exit()
    else:
        print("Invalid input")
        guessCount -= 1  # Decrement the guess count for an invalid input

# Check if the user is cheating
if endingRange < startingRange:
    print("Hmmm something seems off, it looks like you are cheating....")
    
# If the loop is complete without a correct guess
print("You win!")
