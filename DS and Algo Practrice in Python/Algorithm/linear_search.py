def linear_search(arr, length, num):
    for i in range(0, length):
        if(arr[i] == num):
            return i
    return -1

arr = [10,20,30,40,44,55]
lenght = len(arr)
num = int(input("Enter the value you want to search "))

result = linear_search(arr, lenght, num)
# if result == -1:
#     print("Not found")
# else:
#     print("Found at index", result)


print("no" if result  == -1 else "yes")
