# n = int(input())
# magnets =[]
# count=1
# for i in range(n):
#     magnets.append(int(input()))
# for i in range(n-1):
#     if magnets[i] != magnets[i+1]:
#         count = count+1
# print(count)

# n = int(input())
# count=1
# previous = int(input())
# for i in range(1,n):
#     magnet = int(input())
#     if previous != magnet:
#         previous=magnet
#         count +=1
# print(count)

n = int(input())
magnet_list=[]
for i in range(n):
    magnet_list.append(int(input()))
    count =1
    for j in range(n-1):
        if magnet_list[j] == magnet_list[j+1]:
            sole =0
        else:
            count +=1
    print(count)
