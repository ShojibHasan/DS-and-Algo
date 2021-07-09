n = int(input())
data = list(map(int,input().split()[:n]))
lt = [0]*n

for i in range(n):
    lt[data[i]-1] = i+1
for i in lt:
    print(i,sep=' ',end=' ')