lst = list(range(1,100))
for i in lst:
    if i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("buzz")
    elif i % 2 == 0:
        print ("divisible by 2")
    else:
        print (i)