# def isPalindrome(x):
#     num = x
#     reversed_num = 0

#     while num != 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return reversed_num


# print(isPalindrome(121))


# def arry_sort(nums):
#     new_nums = []
#     i = len(nums)-1
#     while i >=0:
#         new_nums = new_nums + [nums[i]]
#         # new_nums.append(nums[i])
#         i-=1
#     return new_nums

# nums = [1,2,3,4,5]
# print(arry_sort(nums))


# print(str(nums)[::-1])

def isPalindrom(x):
    if x <0:
        return False
    
    original = x
    reversed_num = 0
    
    while x!=0:
        digit = x%10
        reversed_num = reversed_num * 10 + digit
        x//=10
    
    return original == reversed_num
        

print(isPalindrom(121))