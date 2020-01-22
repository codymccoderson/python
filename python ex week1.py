# user_input = input("What is your name? ")

# print("Hey " + user_input + "!") 

# user_input = input("What is your name? ")

# user_input2 = user_input.upper()
# lengthofname = str(len(user_input2))

# print("Hello, ".upper() + user_input2 +"!")
# print("Your name has ".upper() + lengthofname + " letters in it!".upper())

# print("Please fill out the blanks below: ")
# name = input("What is name? ")
# subject = input("What is subject? ")
# print(name.title() +"'s" + " favorite subject in school is " + subject.lower() +".")

day = int(input('Day (0-6)? '))
if day == 0:
    print('Monday')
elif day == 1:
    print('Tuesday')
elif day == 2:
    print('Wednesday')
elif day == 3:
    print('Thursday')
elif day == 4:
    print('Friday')
elif day == 5:
    print('Saturday')
elif day == 6:
    print('Sunday')
else:
    print('Please enter a number 0-6. ')




# 7. Tip Calculator

#bill_total = int(input('How much was your bill? '))
#service = input( 'How was your service? good, fair, bad? ').lower()
#if service == 'good':
#    tip_amount = bill_total * 0.2
#elif service == 'fair':
#    tip_amount = bill_total * 0.15
#elif service == 'bad':
#    tip_amount = bill_total * 0.10
#else:
#    print('Please indicate service as good, fair, or bad.')
#total = bill_total + tip_amount
#print('Tip Amount: ${:.2f}'.format)