from logo import * 


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print (logo) 

def caeser(text, shift, direction):
    newText = ""

    if direction == 'decode':
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + shift
            newText += alphabet[newPosition]
        else:
            newText += char 

    print(f"the {direction}ed text is {newText}.") 


letContinue = True
while letContinue:
    direction = input("type 'encode' to encode message or 'decode' to decode message.\n") 
    text = input ("Type your message here.\n").lower()
    shiftValue = input("What's your shift value?\n")
    shiftPosition = shiftValue % 26 #used if shift value is too big.


    caeser(text=text, shift=shiftValue, direction=direction)

    result = input ("Type 'yes' to cintinue or 'no' to discontinue.")
    if result == 'no':
        letContinue = False
        print ("Goodbye. Stay paranoid.")
    else:
        letContinue = True