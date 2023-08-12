#importing time module for time.sleep() function. 
import time 

# this function checks if a number is a prime number
# it is executed on choice == 1:
def primeChecker (num):
    if num<1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def primeLister(start, end):
    #we pass the function an empty array which will be filled by prime number from the program
    primes = []

    #iterates over the given range until ending number
    for num in range(start, end +1):
        
        #we use the first function to check if listed numbers are primes
        if primeChecker(num):
            #this line adds a number to the empty array if it is found to be a prime number
            primes.append(num)
    return primes 



#Prompting users for inputs
print("What do you want to do?\n 1. Check if a number is prime.\n 2. List prime numbers between given numbers. ")
time.sleep(2)

#taking user choice
choice = int(input("Enter your choice by pressing 1 or 2 and pressing Enter"))

#this if else block checks users inputs and calls appropriate functions to execute
if choice==1:
    num = int(input("Enter a number: "))
    primeChecker(num)
    if primeChecker(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

elif choice==2:
    start = int(input("Enter the first number. preferably a smaller number than the second input"))
    end = int(input("Enter the last number. Preferably a bigger number than the first. BUT WHATEVER!"))
    prime_numbers = primeLister(start, end)
    #print("Primes between", start, "and", end, "are:", prime_numbers)
    
    #this line print each prime number on a new line for easier readability.
    for prime in prime_numbers:
        print (prime)
    
    #primeLister(start, end)

#if choice wasn't 1 0 2, end up here and program exits
else:
    print("You must've really fucked up the program or you just can't read if you are seeing this output")
    exit()