def binary_search(L,x):
    left,right =0,len(L)-1

    while left <= right:
        mid =(left+right)//2

        if L[mid] ==x:
            return mid

        if L[mid] <x:
            left = mid+1
        else:
            right = mid-1
    return -1

print(binary_search([1,4,6,7,10,19,22,23,30,35,39,46,50],10))