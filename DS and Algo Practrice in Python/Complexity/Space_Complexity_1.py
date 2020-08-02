'''
n =input()
n = int(n)

if n%2==0:
    print(n,"is a even number")

else:
    print(n,"is a odd number")

#Space Complexity O(1)
'''


n=100
even = [False]*(n+1)
for i in range(0,n+1,2):
    even[i]=True

# Space Complexity O(n)
# Space/memory depends on " n "





