class Solution:
    def removeElement(self, nums, val):
        r =0
        i =0
        while i < len(nums):
            if nums[i] != val:
                nums[r] = nums[i]
                r += 1
            i+=1
nums = [0,1,2,2,3,0,4]
val =2
solve = Solution()
solve.removeElement(nums,val)
print(nums)