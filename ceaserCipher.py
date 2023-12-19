#  File: ceaserCipher.py
#  Author: Ahmed Hussein
#  Date: 12/10/2023
#  Description: A program to take in an encoded ceaserCipher string and decode it based on a dictionary

#  Input/Output:
    #Input: An encoded string
    #Process: Take the encoded string and decode it by going through 25 possible rotations then save those possible rotations in a set. Then compare that set to the provided dictionary
    #Output: A possible decoding of the string based on the comparision between the dictionary and the possible rotations sets. 
    
#  Pseudocode:
    #1. Divide the program into functions, one to load the dictionary and strip it into words, one to do the decryption and a main funtion to put everything together  
    #2. For decrypting the text use this tutorial https://likegeeks.com/python-caesar-cipher/
    #3. Create two sets one for the outcomes of the decrypt function (possibleRotationsSet) and another one for the words that are found after the comparision of the possibleRotationsSet and the dictionary
    #4. Print the foundWords set


# Different sets to store data.
possibleRotationsSet = set()
foundWords = set()
incorrectRotations = set()

# function to load the dictionary and strip it into words for future comparision 
def loadDictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip() for word in file)

# Decryption function which takes in the ciphereText and the shift. The shift is obviously going to be chaning through looping through the 26 rotations 
def decrypt(ciphertext, shift):
    decryptedText = ""
    for char in ciphertext:
        newChar = chr((ord(char) - ord('a') + shift ) % 26 + ord('a'))
        decryptedText += newChar
    return decryptedText

# main function to put everything togther 
def main():
    # dictionary = loadDictionary('temp.txt')
    dictionary = loadDictionary('words_alpha.txt')
    cipherText = input("Enter the ciphertext: ")
    # loop through the possible rotations and then add the 25 rotations to the possibleRotationsSet
    for shift in range(26):
        decryptedText = decrypt(cipherText, shift)
        possibleRotationsSet.add(decryptedText)
    # check if the word is in the dictionary using the possibleRotationSet and then add the ones found to the foundWordsSet
    for possibleRotation in possibleRotationsSet:
        if possibleRotation in dictionary:
            foundWords.add(possibleRotation)
        else:
            # had to create an incorrectRotations Set because the program wouldn't work with return statement 
            incorrectRotations.add(possibleRotation)

    print("Possible Words: ", foundWords)

main()