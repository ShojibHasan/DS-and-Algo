def singleNumber(nums):
    
    duply = []
    for i in nums:
        if i in duply:
            duply.remove(i)
        else:
            duply.append(i)
    return int(duply[0])

a = singleNumber([4,1,2,1,2])
print(a)