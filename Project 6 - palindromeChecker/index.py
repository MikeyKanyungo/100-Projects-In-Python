s = input("enter a string: ")

def is_palindrome (string):
    
    for i in range(1, int(len(string) / 2)):
        if string[i] == string[len(string) - i - 1]:
            return True
        return False


print (is_palindrome(s))