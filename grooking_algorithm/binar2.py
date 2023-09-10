def binary_search(list,item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low+high)//2
        print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            mid = high - 1
        else:
            mid = high + 1
    return None

list = [1,2,3,4,5,6,7,8,9,10]
item = 7         
a  = binary_search(list,item)
print(a)