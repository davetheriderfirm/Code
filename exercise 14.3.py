import os
import shelve

def md5_file(filename):
    cmd = "CertUtil -hashfile " + "'" + filename + "'" " MD5"
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return(res)

def check_shelf(filepath, filename):
    '''Check if the current file md5sum is already in the shelf.
        If it is, print the current filepath and the one whose md5sum it matches.
        Otherwise, add it to the shelf.'''
    try:
        dupfile = shelf[md5_file(filename)]
        print(dupfile)
        print(filepath)
    except KeyError:
        shelf[md5_file(filename)] = filepath

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            root_ext = os.path.splitext(path)
            if root_ext[1] == '.mp3':
                check_shelf(path, name)
        else:
            walk(path)

#def os_walk(dirname):
#    for root, dirs, files in os.walk(dirname):
#        for filename in files:
#            print(os.path.join(root,filename))

shelf = shelve.open('mymp3s', 'c')

absolute_path = '/Users/random/Music'
walk(absolute_path)
shelf.close()
