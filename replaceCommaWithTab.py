#  File: replaceCommaWithTab.py
#  Author: Ahmed Hussein
#  Date: 10/16/2023
#  Description: The program asks the user for a file path that contains comma seprated values and using a funtion prints out a text with each comma replaced by a tab

#  Input/Output:
    #Input: A path to a file with comma seprated values
    #Process: Reads the file and replaces the commas by tabs
    #Output:  The values seprated with a tab instead of a comma
    
#  Pseudocode:
    # 1. Open the file using the file path provided by the user
    # 2. using a function read every line in the file then seprate replaces each comma with a tab
    # 3. print out the line with the commas replaced with tabs

# Open the file
filePath = input("Enter the path to the file: ")
file = open(filePath, "r")

# Function to replace each comma with a tab. 
def replace(file):
    for line in file:
        print(line.strip().replace(",", "\t"))

replace(file)

#  wait for input from the user to close the program
input("Press enter to close the program")