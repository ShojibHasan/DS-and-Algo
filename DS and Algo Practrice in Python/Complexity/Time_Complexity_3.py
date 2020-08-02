n = input()
n = int(n)

count =0

for i in range(1,n+1):
    for j in range(1,n+1):
        count = count+1  # Time Complexity = O(n^2)

for q in range(1,n+1):
    count = count+1 # Time Complexity = o(n)

print("Count = ",count)

# Total Time Complexity = O(n^2+n) or We can say = O(n^2)