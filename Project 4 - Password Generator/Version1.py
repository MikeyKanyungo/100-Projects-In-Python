import random
passlen = int(input("How long do you want your password to be?"))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSVWXYZ09123456789!@$%^&*()_+?/>.<,':;"
p = "".join(random.sample(s,passlen))
print(p)