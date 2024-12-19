def length_of_last_word(s):
    # Strip any trailing spaces and split the string into words
    words = s.strip().split()
    
    # Return the length of the last word
    return len(words[-1])

# Example 1
s ="   fly me   to   the moon  "
print(length_of_last_word(s))  # Output: 5
