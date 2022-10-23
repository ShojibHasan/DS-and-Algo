class Solution:
    def lengthOfLongestSubstring(self, s):
        empty_list = ""
        
        for i in s:
            if i not in empty_list:
                empty_list = empty_list+i
        return len(empty_list)
    
    
h = Solution()
s = "pwwkew"
print(h.lengthOfLongestSubstring(s))
