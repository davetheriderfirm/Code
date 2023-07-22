fin = open('words.txt')

def avoids(word, forbidden):
    """If any of the letters in forbidden appear in word, return False. Otherwise return True"""
    for letter in word:
        if letter in forbidden:
            return False
    return True

total = 0
total_avoid = 0
avoidstring = input('> ')

for line in fin:
    total += 1
    nextword = line.strip()
    if avoids(nextword, avoidstring) == True:
        #print(nextword)
        total_avoid += 1

print('percentage ' , (total_avoid * 100 / total))


