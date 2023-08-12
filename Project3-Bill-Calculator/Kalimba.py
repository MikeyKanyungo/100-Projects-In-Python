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

# Calculate the number of paying children
paying_children = children - below

# Calculate the number of adults entering for free (1 free adult for every 10 paying children)
free_adults = paying_children // 10

# Calculate the earned discount for every 50 paying children (5% discount)
discount_amount = (paying_children // 50) * (entry_children * 0.05)

# Calculate the total bill for adults and children
bill_adults = (adults - free_adults) * entry_adults
bill_children = paying_children * entry_children

# Calculate the total bill to be paid
total_bill = bill_adults + bill_children - discount_amount
print ("Your total bill is K", total_bill)