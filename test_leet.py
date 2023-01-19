def removeElement(nums,vals):
    i =0
    j =0
    while i <len(nums):
        if nums[i]!=vals:
            nums[j]=nums[i]
            j+=1
        
        i+=1
    return j
    
nums = [3,2,2,3]
vals= 3
a = removeElement(nums,vals)
print(a)