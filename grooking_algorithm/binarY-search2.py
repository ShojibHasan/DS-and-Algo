def binary_search(list,target):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        
        if guess == target:
            return mid
        elif guess > target:
            high = mid-1
        else:
            low = mid+1

list = [11,22,33,44,55,66,77,88,99,111,122,133,144,155,166,177,188,199]
target = 111
print(binary_search(list,target))
            