class Solution:
    def twoSum(self, nums, target):
        left =0
        right= len(nums)-1
        for i in range(len(nums)):
            if nums[left] + nums[right]== target:
                return left,right
            elif nums[left] + nums[right] >=target:
                right -=1
            elif nums[left] + nums[right] <= target:
                left +=1
                
                
                
# a = [1,2,3,4,5,6,7,8,9,10]
# target = 5

# start =0
# end = len(a)
# while start<end:
#     if a[start]==target:
#         print("found")
#     start+=1