# File: subnetMaskCalculator.py
# Author: Ahmed
# Date: 12/11/2023
# Description: A program to check if two IP addresses are on the same subnet

# Input/Output:
#   Input: Two IP addresses and subnet mask
#   Process: Check if addresses are on the same subnet
#   Output: Print whether addresses are on the same or different subnets

# Pseudocode:
#   1. Take in the first and second IP addresses
#   2. Take in the subnet mask
#   3. Convert octets of IP addresses and subnet mask to integers
#   4. Loop through each octet to check if addresses are on the same subnet
#       a. Compare between (octet 1& octet3) and (octet2 & octet3)   Bitwise AND: https://stackoverflow.com/questions/3427585/understanding-the-bitwise-and-operator
#   5. If loop completes without returning False, return True
#   6. In the main function, take user input for IP addresses and subnet mask
#   7. Call the areTheyOnTheSameSubnet function and print the result


# The function that devides the ips and subnetmask into octets then does the comaprison. If the comparison returns true then they are on the same subnet
# if not then they are not
def areTheyOnTheSameSubnet(ip1, ip2, subnetMask):
    ip1Octets = [int(octet) for octet in ip1.split('.')]
    ip2Octets = [int(octet) for octet in ip2.split('.')]
    maskOctets = [int(octet) for octet in subnetMask.split('.')]

    for octet1, octet2, octet3 in zip(ip1Octets, ip2Octets, maskOctets):
        if (octet1 & octet3) != (octet2 & octet3):
            return False
    return True

def main():
    ip1 = input("Enter the first IP address: ")
    ip2 = input("Enter the second IP address: ")
    subnet_mask = input("Enter the subnet mask: ")

    if areTheyOnTheSameSubnet(ip1, ip2, subnet_mask):
        print("The addresses are on the same subnet.")
    else:
        print("The addresses are on different subnets.")

if __name__ == "__main__":
    main()
