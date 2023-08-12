import secrets 
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = int(input("How long do you want your password to be?"))

pwd = ' '

for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print (pwd)