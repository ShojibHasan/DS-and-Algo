from operator import le


class Solution:
    def strStr(self,haystack,needle):
        # k =0
        # j=0
        
        # while k< len(haystack):
        #     if needle[j]==haystack[k]:
        #         j+=1
        #         k+=1
        #         if j==len(needle):
        #             break
        #     else:
        #         j=0
        #         k+=1
        # if j==len(needle):
        #     return 0
        # else:
        #     return -1
        index =-1
        for i in range(0,len(haystack)):
            str1 = haystack[i:i+len(needle)]
            if str1==needle:
                index=i
                break
        return index
                
                
            
        
        
a = Solution()

haystack = "leetcode"
needle = "leeto"
value = a.strStr(haystack,needle)
print(value)