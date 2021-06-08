n, m = map(int,input().split())
price = list(map(int,input().split()[:n]))
price.sort()
count = 0
for i in range(n):
    if price[i] <= 0 and i<m:
        count += price[i]
print(-1*(count))