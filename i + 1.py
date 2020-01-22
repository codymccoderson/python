word = input("Type a word. ")
count = 0
vowel_string2 = ""
vowels = "aeiou"

while count < len(word):
    if (word [count] in vowels):
        if (word [count] == word [count + 1]):
            vowel_string2 += (word [count] * 4)
        else:
            vowel_string2 += word [count]
    else:
        vowel_string2 += word [count]
    
    count += 1

print(vowel_string2)
