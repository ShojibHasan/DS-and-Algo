name_value = input()
name_value=set(name_value)
s="".join(name_value)

t=""
for i in name_value:
    if(i in t):
        pass
    else:
        t=t+i
t_len = len(t)
if t_len % 2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
