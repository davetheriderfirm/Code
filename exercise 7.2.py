import math

def eval_loop():
    save_line = 0
    while True:
        line = input('> ')
        if line == 'done':
            return save_line
        save_line = eval(line)
        print(save_line)
        
print(eval_loop())