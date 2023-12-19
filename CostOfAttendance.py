#  File: CostOfAttendance.py
#  Author: Ahmed Hussein
#  Date: 12/10/2023
#  Description: A program to calculate the cost of attendance at CMCC 

#  Input/Output:
    #Input: Number of Credits, Weather if they are in-state or out-of-state, where they live, estimated cost of books and supplies, estimated cost of miscellaneous costs. 
    #Process: 
    #Output:
    
#  Pseudocode:
    #1.
    #2. 
    #3. 

credits = int(input("Enter the number of credits you are taking: "))
inStateResident = input("Are you a Maine Resident? (y/n): ")
onCampusHousing = input("Do you live on Campus? (y/n): ")


def calculateTotalCost(credits, inStateResident, onCampusHousing, housingHall, miscellaneousCost, booksCost):
    tuition = 94 * credits
    if inStateResident.lower() == 'y':
        mandatoryFees = 984
    else:
        tuition = tuition + 2880
        mandatoryFees = 984  

    if onCampusHousing.lower() == 'y':
        if housingHall == "Rancourt Hall":
            housingCost = 10000
        elif housingHall == "Fortin Hall":
            housingCost = 9340
        elif housingHall == "Apartments":
            housingCost = 10698
        elif housingHall == "Mustang Hall":
            housingCost = 10698
    else:
        housingCost = 0

    total = tuition + mandatoryFees + housingCost + miscellaneousCost + booksCost

    return total


def main():
    if onCampusHousing.lower() == 'y':
        housingHall = input("Which on-campus hall are you living in? (Rancourt Hall, Fortin Hall, or Apartments): ")
    else:
        housingHall = None
    booksCost = float(input("Enter an estimated cost of your books and supplies: "))
    miscellaneousCost = float(input("Enter an estimated cost of your miscellaneous expenses: "))
    total = calculateTotalCost(credits, inStateResident, onCampusHousing, housingHall, miscellaneousCost, booksCost)
    print("Your total cost of attendance for one year is: $", total)

main()
