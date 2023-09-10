
def remove_duplicate(nums):
    n = len(nums)
    # unique_nums = [0]*n
    # print('unique_nums: ', unique_nums)
    # unique_nums[0] = nums[0]
    current_index = 1
    for i in range(1,n):
        if nums[i] != nums[i-1]:
            nums[current_index] = nums[i]
            current_index +=1
    return current_index

a = remove_duplicate([1,2,2,3,4,4,5,6,7,7,8,9])
print(a)