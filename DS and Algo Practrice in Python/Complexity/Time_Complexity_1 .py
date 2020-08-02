# Addition of Integer Number 1 to N

# Code: 1
n =input()
n = int(n)
result = n*(n+1)/2 # time complexity =O(1)
print(result)



# Code: 2

n = input()
n = int(n)
result = 0 # Assingment Operation =1
for i in range(1,n+1):
    result = result+i # TIME COMPLEXITY = O(n)
print(result)




