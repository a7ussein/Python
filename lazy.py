import sys

VOWELS = ('a', 'e', 'i', 'o', 'u')
# Functionn to add the syllabel hay to any word that beings with a vowel. if the word doesn't start with a vowel
# then the first letter is moved to the end of the word and then add the syllabel ay 
def convert_word(word):
    first_letter = word[0]
    if first_letter in VOWELS:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"   
# Function to check each word in a sentence then adds hay or ay based on the vowels. 
def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    print(list_of_words)
    new_sentence = ""
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word) + " "  
    return new_sentence

print ("Type in a sentence please")
sentence =  sys.stdin.readline()
print (convert_sentence(sentence))

