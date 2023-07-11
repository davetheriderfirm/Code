def right_justify(s):
    no_spaces = 70 - len(s)
    print((' ' * no_spaces) + s)
    
right_justify('sausages')