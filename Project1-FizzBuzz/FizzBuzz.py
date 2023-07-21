lst = list(range(1,101))
for i in lst:
    if i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("buzz")
    else:
        print (i)