n = int(input()) 
arr = [] 
for i in range(1,n+1): 
    arr.append(i) 

strings = [str(integer) for integer in arr]
a_string = "".join(strings)
an_integer = int(a_string)

print(an_integer)