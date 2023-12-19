encodedText = input("Enter your encoded message: ")
message = ""
for numStr in encodedText.split():
    num = int(numStr)
    message += chr(num)
print("Decoded message: ", message)