'''
n = input()
n = int(n)
count =0

for i in range(1,n+1):
    for j in range(1,n+1):
        count =count+1 # Complexity = O(n^2)

print("N= ",n,"Count = ",count)

# value of "Count" depending on value of " n " . "count" is square of " n "
# Complexity = O(n^2)
'''

p = input()
p = int(p)
count =0

for i in range(1,p+1):
    for j in range(1,p+1):
        for q in range(1,p+1):
            count = count+1 # Complexity = O(n^3)
print("N= ",p,"Count = ",count)

# value of "Count" depending on value of " p " . "count" is qube of " p "
# Complexity = O(n^3)

#Note: Normally n^3 is the Height complexity . If n^4 is come there is something wrong