# message = input().replace(" ","").lower()

# usedChars=[]

# frequences = {}

# for character in range(len(message)):
#     #print(f"Current Char: {message[character]}")
#     if message[character] not in usedChars:    
#         usedChars.append(message[character]) 
#         count = 0
#         for i in range(character,len(message)):
#             if message[i] == message[character]:
#                 count+=1
#             frequences[message[character]] = (count/len(message))*100
            
# print(frequences)
# values = list(frequences.values())
# values.sort()
# print(values)

from collections import Counter
alphabet = "abcdefghijklmnopSrstuPwxyz "
keyword =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
print("\n")
ciphertext = input("Entered encrypted message (ALL CAPS AND NO SPECIAL CHARACTERS)")
print(Counter(ciphertext))

decoded = ""

        

for letter in ciphertext:
    try:
        position = keyword.index(letter) # find letter in 'keyword'...
        decoded += alphabet[position]
    except ValueError:
        print("[ERROR] Make sure inputed encrypted message is all caps with no special characters")
        exit()

print("\n")

def makeChange(old, new, encrypted):
    for letter in encrypted:
        if letter == old:
            letter == new
    print(f"New Version: {encrypted}")
stop  = False

print(f"Encrypted Message in lowercase: {decoded}")
while stop == False:

    print("What would you like to change (letter to replace) (replacement letter): ")
    print("Ex: e A")
    old, new = input("").split(" ")
    makeChange(old, new, decoded)
    print("\n")
    choice = input("Would you like to stop (Y/N): ")
    if choice == 'Y':
        stop == True
    else:
        stop == False

