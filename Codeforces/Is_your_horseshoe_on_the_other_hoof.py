colors = list(map(int,input().split()))
value=set()
buy =0
for i in range(len(colors)):
    if colors[i] in value:
        buy +=1
    value.add(colors[i])
print(buy) 