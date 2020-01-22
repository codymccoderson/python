# print("Omg the guy hacked a payphone!".upper())
# print("he could whistle into the phones and cause nuclear war!".capitalize())

# hacker_str = "The hacker was sentenced to 20 years of solitary confinement in prison."

# count = (len(hacker_str) -1)
# while count >= 0:
    # print(hacker_str[count])
    # count -= 1

#paragraph = input("Type a few sentences. ").upper()
#count = 0
#new_string = ""

#while count < len(paragraph):
    #if (paragraph [count] == "a"):
        #new_string += "4"
    #elif (paragraph [count] == "e"):
         #new_string += "3"
#    elif (paragraph [count] == "g"):
#        new_string += "6"
#    elif (paragraph [count] == "i"):
#        new_string += "1"
#    elif (paragraph [count] == "o"):
#        new_string += "0"
#    elif (paragraph [count] == "s"):
#        new_string += "5"
#    elif (paragraph [count] == "t"):
#        new_string += "7"
        
#    else: 
#        new_string += paragraph [count]


#    count += 1        

#print(new_string)

# Extend repeating vowels to a length of 5 in a word.

# word = input("Type a word.  ")
# count = 0
# vowel_string = ""

# while count < len(word):
#     if (word [count] == "a" and word [count + 1] == "a"):
#         vowel_string += "aaaaa"
#     elif (word [count] == "e" and word [count + 1] == "e"):
#         vowel_string += "eeeee"
#     elif (word [count] == "i" and word [count + 1] == "i"):
#         vowel_string += "iiiii"
#     elif (word [count] == "o" and word [count + 1] == "o"):
#         vowel_string += "ooooo"
#     elif (word [count] == "u" and word [count + 1] == "u"):
#         vowel_string += "uuuuu"
#     else: 
#         vowel_string += word [count]
    
#     count += 1

# print(vowel_string)

vowels = 'aeiou'
user = input("ENTER: ")
new_string = ''

for i in range(len(user)):
    if user [i] == user[i -1] and user[i] in vowels:
        new_string += user[i] * 4
    else: 
        new_string += user[i]
print(new_string)