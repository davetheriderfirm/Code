import anagram_sets
import dbm
import pickle

def store_anagrams(anag_map):
    for key, value in anagram_map.items():
        db[key] = pickle.dumps(value)
        
db = dbm.open('myanagrams', 'c')
anagram_map = anagram_sets.all_anagrams('words.txt')
store_anagrams(anagram_map)
