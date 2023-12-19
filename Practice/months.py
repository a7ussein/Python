months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# i = 0
# while i < len(months):
#     month = months[i:i+3]
#     print(month)
#     i = i+3

monthNumber = int(input("Enter a month number (1-12): "))
pos = (monthNumber-1) * 3 
monthAbbrev = months[pos:pos + 3]

print("The month abbrev is: " , monthAbbrev)