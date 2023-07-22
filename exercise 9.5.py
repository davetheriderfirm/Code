fin = open('words.txt')

def uses_all(word, usestring):
    return(uses_only(usestring, word))

def uses_only(word, usestring):
    """If any of the letters in word do not appear in usestring, return False. Otherwise return True"""
    for letter in word:
        if letter not in usestring:
            return False
    return True

total = 0
total_avoid = 0
usestring = input('> ')

for line in fin:
    total += 1
    nextword = line.strip()
    if uses_all(nextword, usestring) == True:
        print(nextword)
        total_avoid += 1

print('percentage ' , (total_avoid * 100 / total))