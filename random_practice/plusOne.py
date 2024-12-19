def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):  # Start from the last digit and move left
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # Set current digit to 0 if it's 9
    
    # If all digits were 9, we need to add a new leading 1
    return [1] + digits

# # Example 1
digits = [4, 3, 2, 1]
# print(plus_one(digits))  # Output: [4, 3, 2, 2]

# # Example 2
# digits = [9]
# print(plus_one(digits))  # Output: [1, 0]

# Example 3
# digits = [9]
print(plus_one(digits))  # Output: [1, 0, 0, 0]
