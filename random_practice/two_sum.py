# def twoSum(nums, target):
#     for i in range(0,len(nums)-1):
#         for j in range(1,len(nums)):
#             if nums[i] + nums[j]== target:
#                 index =[i,j]
#                 return index
    
    


def twoSum(nums,target):
    num_map = {}
    for i,num in enumerate(nums):
        complement = target - num 
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i
        
        
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))


def two_sum(nums,target):
    nums_map ={}
    for i , num in enumerate(nums):
        compliment = target- num
        if compliment in nums_map:
            return [nums_map[compliment],i]
        nums_map[num] = i
        
        
        
