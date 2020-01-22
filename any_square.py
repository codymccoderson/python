# your_square = int(input("How big do you want your square to be homie? Please enter number here: "))

# for i in range (your_square):
#      for j in range (your_square):
#         print("* ", end = "")
#     print()

your_square = int(input("How big do you want your square to be homie? Please enter number here: "))
i = 0

while (i < your_square):
    j = 0
    while (j < your_square):
        j = j + 1
        print("* ", end = "")
    i = i + 1
    print()
