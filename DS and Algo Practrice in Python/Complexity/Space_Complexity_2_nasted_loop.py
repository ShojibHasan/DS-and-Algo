'''
n=input()
n=int(n)

count=0
for i in range(n):
    for j in range(n):
        count +=1
print("n=",n,"count=",count)

# Space Complexity O(n^2)
#Note: count = square of "n" . When we take input , count=+1 statment run by "n^2"


'''

n = input()
n = int(n)
count=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            count +=1
print("n =",n,"Count =",count)

# Space Complexity = O(n^3)