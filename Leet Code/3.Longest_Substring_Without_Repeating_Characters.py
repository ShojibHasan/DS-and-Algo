class Solution:
    def lengthOfLongestSubstring(self, s):
        empty_list = ""
        j=0
        
        for i in s:
            if i in empty_list:
                j=0
            else:
                empty_list = empty_list+i
                j+=1
        return j
    
    
h = Solution()
s = "pwwkew"
print(h.lengthOfLongestSubstring(s))
