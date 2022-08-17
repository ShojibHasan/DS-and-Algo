
def binary_search(list,item):
    low =0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2
        
        guess = list[mid]
        
        if guess == item:
            return mid
        
        if guess>item:
            high = mid-1
            
        if guess<item:
            low = mid+1
    return None




list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
item =8

a = binary_search(list,item)
print(a)


# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# item1 =17
# for i in range(len(list1)):
#     if list1[i] == item1:
#         print(i)