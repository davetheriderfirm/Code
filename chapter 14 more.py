import os
import dbm
import pickle
import wc

db = dbm.open('sausages', 'c')

db['cumberland'] = 'Long and curly'
t = [1,2,3]
db['tuple'] = pickle.dumps(t)

for key in db.keys():
    print(key, db[key])

db.close()

#filename = 'davebook.txt'
#cmd = 'md5sum ' + filename
#fp = os.popen(cmd)
#res = fp.read()
#stat = fp.close()
#print(res)

wc.linecount('wc.py')