# #Remove Duplicates Numbers in a Array

# def remove_duplicates(nums):
#     unique_nums =[]
#     # unique_nums.append(nums[0])
#     # print(unique_nums)
#     n = len(nums)
#     for i in range(0,n):
        
#         if nums[i] != nums[i-1]:
#             unique_nums.append(nums[i])
#     return unique_nums

# nums=[11,11,22,22,33,33,444,33,444]
# print(remove_duplicates(nums))


# def remove_duplicates(nums):
#     unique_nums =[]
#     n = len(nums)
#     for i in range(0,n):
#         if nums[i] != nums[i-1]:
#             unique_nums.append(nums[i])
#     return unique_nums
# nums=[11,11,22,22,33,33,444,33,444]
# print(remove_duplicates(nums))

# def remove_duplicares(nums):
#     # unique_nums =list(set(nums))
#     unique_nums = set(nums)
#     unique_nums = list(unique_nums)
#     unique_nums.sort()
#     return unique_nums

# nums=[11,11,22,22,33,33,444,33,444]

# # list1 =[12,12,33,434,44,22,33,88,90,55,88]
# print(remove_duplicares(nums))

# def remove_duplicates(nums):
#     n = len(nums)
#     unique_nums = [0]*n
#     unique_nums[0] = nums[0]
#     current_index =1
#     for i in range(1,n):
#         if nums[i] != nums[i-1]:
#             unique_nums[current_index] = nums[i]
#             current_index +=1
#     return unique_nums
# nums=[11,11,22,22,33,33,444,33,444]
# print(remove_duplicates(nums))



mylist = [11,11,22,22,33,33,444,33,444]
mylist = list(dict.fromkeys(mylist))
print(mylist)