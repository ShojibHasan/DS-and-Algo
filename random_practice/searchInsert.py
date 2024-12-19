def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # The position where the target would be inserted

# Example 1
# nums = [1, 3, 5, 6]
# target = 5
# print(search_insert(nums, target))  # Output: 2

# Example 2
nums = [1, 3, 5, 6]
target = 2
print(search_insert(nums, target))  # Output: 1

# Example 3
# nums = [1, 3, 5, 6]
# target = 7
# print(search_insert(nums, target))  # Output: 4
