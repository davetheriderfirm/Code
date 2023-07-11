def do_n(fn,n):
    if n <= 0:
        return
    else:
        fn()
        do_n(fn,n-1)
        
def sausages():
    print('sausages')
    
do_n(sausages,3)