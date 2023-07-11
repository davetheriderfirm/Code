def do_twice(f1):
    f1()
    f1()
    
def do_four(f2):
    do_twice(f2)
    do_twice(f2)
    
# do one square's worth of the across row
def print_across():
    print('+', end=' ')
    print('- ' * 4, end='')

# do both squares of the across row, and the terminating '+'
def print_across_row():
    do_twice(print_across)
    print('+')

# do one square's worth of the down row
def print_down():
    print('|         ', end = '')

# do both squares of the down row, and the terminating '|'
def print_down_row():
    do_twice(print_down)
    print('|')

# one full row of the grid consists of an across row plus 4 down rows
def print_grid_two():
    print_across_row()
    do_four(print_down_row)

# complete grid is two full rows plus a terminating across row
do_twice(print_grid_two)
print_across_row()
