class Solution:
    def strStr(self,haystack,needle):
        k =0
        j=0
        
        while k<= len(haystack):
            if needle[j]==haystack[k]:
                j+=1
                k+=1
            else:
                j=0
        if j==len(needle):
            return 0
        else:
            return -1
                
            
        
        
a = Solution()

haystack = "sadbutsad"
needle = "sad"
value = a.strStr(haystack,needle)
print(value)