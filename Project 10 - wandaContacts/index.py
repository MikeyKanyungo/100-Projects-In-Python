#we will use this json module for exporting to a json file. 
import json 

# names and phone numbers will be saved to this phone_book JSON file
phone_book = {}

# enter the number of phone numbers a user wants to save
num = int(input("Entries: "))

#this iterates asking for inputs num times
for i in range(num):
	name = input("Name: ")
	phone_number = int(input("Phone: "))
	phone_book[name] = phone_number

#this line saves data to a json file
with open("phone_book.json", "w") as json_file:
	json.dump(phone_book, json_file)

print ("\nName\t\t\tPhone Number\n")

for name, phone_number in phone_book.items():
	print("{}\t\t\t".format(name, phone_number)) 

search_term = input("\nEnter search term: ")

print ("Search Result: ")
if search_term in phone_book:
	phone_number = phone_book[search_term]
	print("Name: {}, Phone: {}".format(search_term, phone_number))
	
else:
	print ("Name not found")