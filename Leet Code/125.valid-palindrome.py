class Solution:
    def isPalindrome(self, s):
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        # print(s)
        start =0
        end = len(s)-1
        
        while start < end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        
        return True
            
# A man, a plan, a canal: Panama
# race a car
so = Solution()
print(so.isPalindrome("race a car"))