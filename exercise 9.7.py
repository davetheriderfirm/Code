import math

def threeconsdoubles(word):
    double_count = 0
    i = 0
    while i < len(word) - 5:
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
           return True
        else:
           i += 1
    return False

fin = open('words.txt')
for line in fin:
    nextword = line.strip()
    if len(nextword) > 5:
        if threeconsdoubles(nextword):
            print(nextword)