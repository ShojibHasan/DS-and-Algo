# def remove_duplicate_array(arr):
#     ans = []
#     for i in arr:
#         if i not in ans:
#             ans.append(i)
#     return ans
# def remove_duplicate_array(arr):
#     seen = {}
#     result = []
#     for num in arr:
#         if num not in seen:
#             seen[num] = True
#             result.append(num)
#     print("Seen: ",seen)
#     print("Result: ",result)
#     return result

mylist = [11,11,44,22,22,33,33,444,33,444]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# print(remove_duplicate_array([1,5,4,4,1,3,10,7,6,8,8,7]))
    
    
