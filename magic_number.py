# Prompt the user for a number
# Compare that number to the predefined value
# If the numbers match, tell the user they're a mind reader
# If they don't match, tell the user, "Thanks for playing!"

user_input = int(input("What number am I thinking of? "))

MAGICNUMBER = 9

if user_input == MAGICNUMBER: 
    print("ARE YOU A MIND READER?")
else: 
    print("Thanks for playing, that's not correct.")