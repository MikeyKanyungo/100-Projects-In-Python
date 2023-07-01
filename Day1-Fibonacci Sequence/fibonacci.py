a = int(input("Enter Your First Number"))
b = int(input("Enter Your Second Number"))


while a < 10000:
    print (a)
    a, b = b, a+b
print ("Fibonacci, sequences are cool!")

