any_word = input("Type a word. Any word! ")
i = 0
dictionary = {}

for i in any_word:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(str(dictionary))