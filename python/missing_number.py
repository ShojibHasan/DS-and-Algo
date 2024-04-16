# need to find a missing element in an array

def find_missing_element(arr):
    arr = sorted(arr)
    first_element = arr[0]
    last_element = arr[len(arr)-1]
    differance = arr[1] - arr[0]
    differance2 = arr[2] - arr[1]

    if differance == differance2:
        for i in range(first_element,last_element,differance):
            if i+differance not in arr:
                return i+differance

    else:
        main_diff = arr[1] - first_element
        for i in range(first_element,last_element,main_diff+2):

            if i not in arr:
                return i





# arr = [6,3,2,7,1,9,8,4]
# arr = [23,53,83,73,13,33,43]
arr = [64,36,9,25,81,16]
print(find_missing_element(arr))