def topKFrequent(nums, k):
    frequent_value = {}
    for i in nums:
        if i in frequent_value:
            frequent_value[i] += 1
        else:
            frequent_value[i] = 1

    res = list(frequent_value.keys())
    a = sorted(res)

    return a[:k]


print(topKFrequent([4,1,-1,2,-1,2,3],2))

