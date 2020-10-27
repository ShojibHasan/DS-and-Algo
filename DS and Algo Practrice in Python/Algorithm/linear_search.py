
'''
def linear_search(L,x):
    n = len(L)
    i =0

    while i<n:
        if L[i] ==x:
            return i
        i +=1
    i =-1

    return i

'''
'''
def linear_search(L,x):
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i

    return -1


# Time Complexity = O(n)
# Space Complexity = O(1)
'''

def linearsearch(a,element):
    for i in range(len(a)):
        if a[i]==element:
            return i
    return -1
element = int(input())
print(linearsearch([1,2,3,4,5,2,1],2))

