def has_map(nums):
    maps = {}
    
    for i in nums:
        maps[i] = maps.get(i,0)+1
    
    return maps
            
            
nums = [1,2,3,4,5,6,1,2,3,4]
print(has_map(nums))