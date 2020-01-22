start = int(input("Enter your first number: "))
end = int(input("Enter your second number: "))

for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")
