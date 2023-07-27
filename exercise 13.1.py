import string

def split_line(linetext):
    '''take the current line and run through the characters to create a word.
       Ignore punctuation, convert alphabetic characters to lower case. 
       Upon reaching a whitespace character, output the current word and
       begin a new one.'''
    current_word = ''
    for letter in linetext:
        if letter in string.whitespace:
            fout.write(current_word + '\n')
            current_word = ''
        else:
            if letter not in string.punctuation:
                current_word += letter.lower()

#fin = open('davebook.txt')
fin = open('marshals.txt')
fout = open('davebookoutput.txt', 'w')

print(string.punctuation)

for linetext in fin:
    split_line(linetext)

fin.close()
fout.close()
    