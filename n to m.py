user_start = int(input("Enter number here: "))
user_end = int(input("Enter number here: "))

print("Here's your list from {0} to {1}! ".format(user_start, user_end))

for i in range(user_start, user_end + 1):
    print(i, end = " ")