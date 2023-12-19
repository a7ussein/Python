months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]

monthNumber = int(input("Enter a month number (1-12): "))
monthAbbrev = monthNumber - 1
print("The month abbrev is: " , months[monthAbbrev])