import math

def rotate_word(word, offset):
    rotated_word = ''
    for letter in word:
        if ord(letter) + offset > ord('z'):
            rotated_word += chr(ord(letter)+offset-26)
        elif ord(letter) + offset < ord('a'):
            rotated_word += chr(ord(letter)+offset+26)
        else:
            rotated_word += chr(ord(letter)+offset)
    return rotated_word

def all_ord(word):
    for letter in word:
        print(letter, ord(letter))
        
print(rotate_word('sleep',9))
#all_ord('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')