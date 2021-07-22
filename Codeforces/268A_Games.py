n = int(input())
a=[]
b =[]
count =0
for i in range(n):
    data1,data2 = map(int,input().split())
    a.append(data1)
    b.append(data2)

for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            count +=1
print(count)

