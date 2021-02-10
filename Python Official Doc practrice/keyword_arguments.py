def parrot(voltage,state='a stiff', action='voom', type='Norwegian Blue'):
    print("__This parrot wouldn't",action,end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# parrot()                     # required argument missing
parrot(voltage=5.0,)  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument