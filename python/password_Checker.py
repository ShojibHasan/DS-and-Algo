
# valid password filters:
# a) at least 8 character
# b) start with a number
# c) last 2 character must be capital

import re
password = input('Type The Password: ')
password_list = list(password)
password_list_length= len(password)
flag = 0
while True:
    if (password_list_length<8):
        break
    elif not re.search("[0-9]", password_list[0]):
        flag = -1
        break

    elif not re.search("[A-Z]", password_list[password_list_length-1]):
        flag = -1
        break
    elif not re.search("[A-Z]", password_list[password_list_length-2]):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
if flag ==-1:
    print("Not a Valid Password")