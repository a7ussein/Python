#  File: Simulator.py
#  Author: Ahmed Hussein
#  Date: 12/4/2023
#  Description: This program simulates the rolling of two dice then prints out the probablity of the appearance of each number. 

#  Input/Output:
    #Input: nothing
    #Process: Simulates the rolling of two dice 100% through a for loop and a roll_dice() function
    #Output: Prints out each number and the probablity of its appearance. 
    
    
#  Pseudocode:
   #Initialize variables to store results (rolls, frequency)
   #For i from 1 to 6 in steps of 1
   #Call roll_dice() function with no arguments
   #Increment the count by one
   #Calculate probability = count / total rolls
   #Print the result


from random import randint

def roll_dice():
    return randint(1, 6), randint(1, 6)

rolls = []
frequency = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Simulate rolling two 6-sided dice 100 times
for i in range(100):
    roll = roll_dice()
    rolls.append(roll)

# Count the frequency of each roll
for roll in rolls:
    total_number = sum(roll)
    frequency[total_number] += 1

# Calculate and print the observed frequency for each total number
total_rolls = len(rolls)
for total_number, count in frequency.items():
    probability = count / total_rolls
    print(str(total_number) + " = " + str(probability * 100) + "%")
