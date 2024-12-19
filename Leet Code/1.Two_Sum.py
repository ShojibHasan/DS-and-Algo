# class Solution:
#     def twoSum(self, nums, target):
#         s =[]
#         for i in range(len(nums)):
#             temp = target-nums[i]
#             if (temp in s):
#                 return i,s.index(temp)
#             s.append(nums[i])
                
                
                
# a = [1,2,4,5,2,0]
# target = 7

# b = Solution()
# print(b.twoSum(a,target))



# def two_sum(nums, target):
#     nums_dict = {}
#     for i, num in enumerate(nums):

#         diff = target - num
#         if diff in nums_dict:
#             return [nums_dict[diff], i]
#         nums_dict[num] = i

#     return []


# nums = [1,2,4,5,2,0]
# target = 7
# print(two_sum(nums, target))


# nums = [1,2,4,5,2,0]
# target = 7

# for i, num in enumerate(nums):
#     for j, num1 in enumerate(nums):
#         if i<j and num+num1 == target:
#             print(f"[{i}, {j}]")


# myList = [1, 2, 3, 4,5,6,7,8,9,10]
# # myList.reverse()

# i = 0
# j = len(myList)-1

# while i <= j:
#     tem = myList[i]
#     myList[i] = myList[j]
#     myList[j] = tem
#     i += 1
#     j -= 1

# print(myList)


# def function(nums,target):
#   for i in range(0,len(nums)-1):
#     for j in range(1,len(nums)):
#       if nums[i]+nums[j]==target:
#           index=[i,j]
#           return(index)

# nums = [1,2,4,5,2,0]
# target=7
# res = function(nums,target)
# print(res)
          
          
