def do_f(f):
    f()
    f()
    
def print_star():
    print('*')
    
do_f(do_f(print_star))