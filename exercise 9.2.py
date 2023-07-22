fin = open('words.txt')

def no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

total = 0
total_no_e = 0
for line in fin:
    total += 1
    nextword = line.strip()
    if no_e(nextword) == True:
       # print(nextword)
        total_no_e += 1

print('percentage ' , (total_no_e * 100 / total))


