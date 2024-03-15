class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result

    
    
h = Solution()
s = "pwwkew"
print(h.lengthOfLongestSubstring(s))
