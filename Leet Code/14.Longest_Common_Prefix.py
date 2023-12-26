def longestCommonPrefix(strs):
    prefix = []
    str_len = len(strs)
    for vals in range(0,str_len):
        for i in vals:
            if i[0] == i[0+1]:
                print("ok")
        
    
    

strs = ["flower","flow","flight"]
a = longestCommonPrefix(strs)