fin = open('words.txt')

def is_abecedarian(word):
    """If any of the letters are not in alphabetical order, return False. Otherwise return True"""
    last_letter = ''
    for letter in word:
        if letter < last_letter:
            return False
        last_letter = letter
    return True

total = 0
total_abecedarian = 0

for line in fin:
    total += 1
    nextword = line.strip()
    if is_abecedarian(nextword) == True:
        print(nextword)
        total_abecedarian += 1

print('percentage ' , (total_abecedarian * 100 / total))