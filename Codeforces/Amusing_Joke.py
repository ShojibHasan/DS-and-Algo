guest_name = input()
residence_host = input()
all_letters = guest_name+residence_host
pile = input()
count =0
count2=0
for i in pile:
    if i in all_letters:
        count +=1
        all_letters =all_letters.replace(i,'')
    else:
        count2+=1
        
        
        
        
# Python code to demonstrate
# checking of element existence
# using loops and in

# def prompt():
#     message,int1,int2  = input().split()
#     return check_input(commands,message)
    

# def check_input(commands, input_commands):
#     for i in range(len(commands)):
#         if commands[i] == input_commands:
#             return commands[i]
    
# commands =['DISPLAY','INSERT','REMOVE','FIND','REMOVEALL','EXIT']
# a = prompt()
# print(a)
# if a[0]== 'DISPLAY':
#     print("Printing")
# elif a[0] == 'INSERT':
#     print(f"Inserting {a[1]} at position {a[2]}")

# elif a[0] == 'REMOVE':
#     print('Removing')
# elif a[0] == 'FIND':
#     print('Finding')
# elif a[0] == 'REMOVEALL':
#     print('Removing all')
# elif a[0] =='EXIT':
#     print("Exiting")
#     exit()
# else:
#     print("Invalid command")




# L =[]

# FIRST = 1
# END = 1

# def append(X):
#     global L
#     L +=[X]

# def display():
#     for i in range(0, 5):
#         print(L[i],end=" ")

# append(10)
# append(20)
# append(30)
# append(50)
# append(100)

# display()