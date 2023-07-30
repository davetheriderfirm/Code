def sed(pattern_str, repl_str, f1, f2):
    try: 
        fin = open(f1)
    except:
        print('Could not open', f1, 'for input')
    try:
        fout = open(f2, 'w')
    except:
        print('Could not open', f2, 'for output')

    for line in fin:
        outline = line.replace(pattern_str, repl_str)
        try:
            fout.write(outline)
        except:
            print('Could not write to', f2)

    try:
        fin.close()
    except:
        print('Could not close', f1)
    
    try:
        fout.close()
    except:
        print('Could not close', f2)
    
sed('the', 'sausages', 'davebook.txt', 'davebookchanged.txt')