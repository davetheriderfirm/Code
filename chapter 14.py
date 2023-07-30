import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

def os_walk(dirname):
    for root, dirs, files in os.walk(cwd):
        for filename in files:
            print(os.path.join(root,filename))

cwd = os.getcwd()
print(cwd)
#os_walk(cwd)
try:
    fin = open('bad_file')
except:
    print('WTF?')