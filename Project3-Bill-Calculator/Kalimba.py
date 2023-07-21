'''
Kalimba Reptile Farm Charges as Entry Fees:
*K80: Adults
K50: Children
Free: Children 2 years and below.

Conditions: 
*For every 10-Paying Children, One adult will enter for free
*There is a 5% Discount for every 50 paying children

TASK:
Write a program that calculates the bill that must be paid 
based on the number of kids, adults and children below 2 years.
'''
#fixing charges
entry_children = 50
entry_adults = 80

#Taking user input data
adults = int(input("How many adults are in your group?"))
children = int(input("How many children did you bring altogether?"))
below = int (input("How many children are 2 years or below?"))

#Function to calculate children that'll be required to pay
def paying_children():
    children - below

    return paying_children

#Function to calculate adults entering for free
def free_adults():
    paying_children / 10

    return free_adults

#Function to calculate earned discount for every 50 children
def discount():
    (paying_children / 50) * 0.05 #0.05 already calculated from 50/100 to simply the calculations

    return discount
print ("You've received", discount, "total")

def bill_adults():
    (adults - free_adults) * 80

    return bill_adults
print("Adults will pay K", bill_adults)

def bill_children():
    paying_children*50

    return bill_children
print("Children will pay", bill_children)

#Function to calculate the total bill to be paid
def total_bill():
    bill_adults+bill_children-discount
    return total_bill

print ("Your total bill is K", total_bill)