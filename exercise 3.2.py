def do_twice(f,mystring):
    f(mystring)
    f(mystring)
    
def print_spam():
    print('spam')
    
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
def do_four(f2,mystring2):
    do_twice(f2,mystring2)
    do_twice(f2,mystring2)
    
do_four(print_twice,'spam')