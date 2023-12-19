#  File: isHiku.py
#  Author: Ahmed Hussein
#  Date: 10/16/2023
#  Description: The program takes in a file path as an input then opens it and checks if the three lines of the file
# that was passed in have a hiku or not


#  Input/Output:
    #Input: A file path, number of syllables in each list of words that are in a line. 
    #Process: Opens the file, reads the first three lines, split each line into words and puts it
    # in a list, the asks the user for the number of syllables in each line and based on the provided funtion figures out if the program has a hiku or not
    #Output: if the first three lines in a file have a hiku or not. 


# Pseudocode:
    # 1. Open the file using the file path provided by the user
    # 2. Read the first three lines of the file
    # 3. for each line, split the line into a list of words
    # 4. for each word in the list, ask the user to input the number of syllables in the word. 
    # 5. check if the number of syllables for each line matches the patter for a valid Hiku.
    # 7. if it does, print out "valid Haiku". Otherwise, print "Not a valid Haiku".
    
# Open the file using the file path provided by the user
filePath = input("Enter the path to the file: ")
file = open(filePath, "r")
lines = []

#Read the first three lines of the file
for i in range(3):
    lines.append(file.readline().strip())

#for each line, split the line into a list of words 
for i in range(len(lines)):
    lines[i] = lines[i].split()
#ask the user for the number of syllables in each line and store it in a list.
syllables = []
for line in lines:
    syllables.append(int(input("Enter the number of syllables in " + str(line) + ": ")))

#check if the number of syllables for each line matches the patter for a valid Hiku.
def isHiku (firstLine, secondLine, thirdLine):
    if (firstLine == 5 and secondLine == 7 and thirdLine == 5):
        return True
    return False
print("The file contains a Hiku:", isHiku(syllables[0],syllables[1],syllables[2]))  

#  wait for input from the user to close the program
input("Press enter to close the program")