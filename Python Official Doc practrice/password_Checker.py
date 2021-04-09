# valid password filters:
# a) at least 8 character
# b) start with a number
# c) last 2 character must be capital

import re

passowrd= input("Input your password: ")
x = True
while x:  
    if (len(passowrd)<8):
        break
    elif not re.search("[0-9]",passowrd):
        break
    elif not re.search("[A-Z]",passowrd):
        break
    elif re.search("\s",passowrd):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
