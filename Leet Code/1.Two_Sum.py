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