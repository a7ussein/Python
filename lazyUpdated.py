import string

VOWELS = ('a', 'e', 'i', 'o', 'u')

def convert_word(word):
    # Extract punctuation mark, if any, from the word
    punctuation = ''
    if word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word[:-1]
    
    first_letter = word[0]
    if first_letter.lower() in VOWELS:
        return word + "hay" + punctuation
    else:
        return word[1:] + first_letter + "ay" + punctuation

def convert_sentence(sentence):
    # Split the sentence into words and apply Pig Latin conversion to each word
    words = sentence.split()
    pig_latin_words = [convert_word(word) for word in words]
    # Join the words back into a sentence
    pig_latin_sentence = ' '.join(pig_latin_words)
    return pig_latin_sentence

print("Type in a sentence please")
sentence = input()
print(convert_sentence(sentence))
