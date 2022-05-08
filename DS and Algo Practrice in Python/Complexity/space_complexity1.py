n = 100
even = [False] *(n+1)
for i in range(0, n+1,2):
    even[i] = True
print(even[4])