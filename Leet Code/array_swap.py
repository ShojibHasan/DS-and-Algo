a = [1,2,3,4]

start = len(a)-1
b =[]

while start>=0:
    b.append(a[start])
    start-=1
print(b)