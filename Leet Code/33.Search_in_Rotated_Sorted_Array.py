


def search(nums,target):
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        if nums[mid] >= nums[low]:
            if target > nums[mid] or target<nums[low]:
                low = mid+1
            else:
                high = mid-1
        
        else:
            if target<nums[mid] or target>nums[high]:
                high = mid-1
            else:
                low = mid+1
    return -1
    
nums = [4,5,6,7,0,1,2]
target = 0
a = search(nums,target)

print(a)