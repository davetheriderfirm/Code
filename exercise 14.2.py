import anagram_sets
import dbm
import pickle

def store_anagrams(anag_map):
    for key, value in anagram_map.items():
        db[key] = pickle.dumps(value)

def read_anagrams(inword):
    try:
        outlist = db[inword]
    except:
        print(inword + ' is not in the wordlist.')
        return
    print(pickle.loads(outlist))
        
db = dbm.open('myanagrams', 'c')
anagram_map = anagram_sets.all_anagrams('words.txt')
store_anagrams(anagram_map)

read_anagrams('nest')

db.close()
