import string, random

char = string.printable
char = char[:len(char)-6]
length = 40
pw = ""
for i in range(length):
    pw += char[random.randint(0,len(char)-1)]
keyIndex = random.randint(0,length)
pw = pw[:keyIndex] + "[" + pw[keyIndex:]
print(pw)


"""
retirer le signe d'indication de la liste char
mettre le signe d'indication au debut
faire en sorte de fermer l'indication

"""