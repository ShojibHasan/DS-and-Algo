n = int(input())
magnets =[]
count=1
for i in range(n):
    magnets.append(int(input()))
for i in range(n-1):
    if magnets[i] != magnets[i+1]:
        count = count+1
print(count)

# n = int(input())
# count=1
# previous = int(input())
# for i in range(1,n):
#     magnet = int(input())
#     if previous != magnet:
#         previous=magnet
#         count +=1
# print(count)