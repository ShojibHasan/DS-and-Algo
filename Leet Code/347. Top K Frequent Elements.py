def topKFrequent(nums, k):
    temp = []
    ans = []
    for i in nums:
        if i not in temp:
            temp.append(i)
    
        if len(ans)==k:
            break
    return ans
            

a = topKFrequent([3,0,1,0],1)

print(a)