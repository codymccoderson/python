# User inputs the battle command to be encrypted.
# User inputs the amount of spaces the characters are shifted.
#
#
#

battle_command = input("Give a command: ").lower()
encrypted_command_string = ""
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
count = 0

while count < len(battle_command):
    if (battle_command in alphabet): 
        (battle_command [count] == (battle_command [count + 4])
    encrypted_command_string += (battle_command [count])
    count += 1
print(encrypted_command_string)
