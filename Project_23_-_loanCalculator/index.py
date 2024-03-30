import os
import time

print("Welcome to Python Loans.")
time.sleep(5)
os.system('cls')

print("Step 1: ")
principle = int(input("Enter your desired amount"))
os.system('cls')

print("Step 2: ")
period = int(input("Choose your desired loan term. \n 1. 3 Months or Less \n 2. 6 Months or Less \n 3. 1 Year or Less \n 4. 5 Years or less. \n\n Enter your choice:  "))
os.system('cls')

print ("Step 3: ")
print("Calculating your loan rate. Please wait.")
time.sleep(3)
os.system('cls')

if period == 1:
    print("You will bw charged 10% interest rate")
    interest = (principle*10*(3/12))/100
    print("Your interest will be K",interest)
    print("Your total payable will be",principle + interest)

elif period == 2:
    print ("You will be charged 20% interest rate.")
    interest = (principle*20*(6/12))/100
    print("Your interest will be K",interest)
    print("Your total payable will be",principle + interest)

elif period == 3:
    print("You will be charged 40% interest rate.")
    interest = (principle*40*1)/100
    print("Your interest will be K",interest)
    print("Your total payable will be K",principle + interest)

elif period == 4:
    print("You will be charged 80% interest rate.")
    interest = (principle*80*5)/100
    print("Your interest will be K",interest)
    print("Your total payable will be K",principle + interest)

else:
    print("Invalid option.")