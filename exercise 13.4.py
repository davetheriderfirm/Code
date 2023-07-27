import string

def split_line(linetext,bookhist):
    '''Take the current line and replaces any hyphens with spaces.
       Then split into words using space as a delimiter.
       Strip whitespace and punctuation from before and after the words,
       and convert to lower case.'''
    linetext = linetext.replace('-', ' ')
    for word in linetext.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        bookhist[word] = bookhist.get(word, 0) + 1

def common_hist(hist):
    tuplist = []
    for key, value in hist.items():
        tuplist.append((value, key))
    tuplist.sort(reverse=True)
    return tuplist

def compare_dicts(d1, d2):
    dictout = {}
    for key in d1:
        if key not in d2:
            dictout[key] = None
    return dictout
                
#fin = open('davebook.txt')
fin = open('marshals.txt')
wordin = open('words.txt')

worddict = {}
bookhist = {}

for word in wordin:
    word = word.strip()
    worddict[word] = None

for linetext in fin:
    split_line(linetext,bookhist)

fin.close()
print(sum(bookhist.values()), 'total words')
print(len(bookhist), 'different words')

tuplist = common_hist(bookhist)
for freq, word in tuplist[:200]:
    print(word, 'appears', freq, 'times')

different_words = compare_dicts(bookhist, worddict)
for word in different_words:
    print(word)