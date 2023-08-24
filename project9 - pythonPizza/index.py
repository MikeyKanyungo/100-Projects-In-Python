bill = 0
print ("Welcome to python pizza. May I take your order please?")
order = input("Enter L for large. M for medium and S for small.")

if order == 'L':
    bill =250
elif order == 'M':
    bill = 200
elif order == 'S':
    bill = 150
elif bill == '':
    print ("please pick your order")
else:
    exit()

print ("Your ", order, " pizza will cost you K", bill)
print ("Would you like some add ons?")
addons = input("Enter 'Y' for yes \nEnter 'N' for no:")

if addons == 'Y':
    addon = input("Pick 'S' to add pepperoni to your small pizza \npick 'M' to add pepperoni to your medium pizza \npick 'L' to add pepperoni to your large pizza")
    if addon == 'S':
        if order == 'S':
            bill += 20
        else:
            print("You did not pick a small pizza.")

    elif addon == 'M':
        if order == 'M':
            bill += 40
        else:
            print("You did not pick a medium pizza.")
    elif addon == 'L':
        if order == 'L':
            bill += 60
        else:
            print("You did not pick a large pizza.")
else:
    print(bill)

print ("Extra cheese?")
extra_cheese = input("Enter 'Y' for Yes. \nEnter 'N' for No.")

if extra_cheese == 'Y':
    bill += 30
else:
    exit()

print (bill)