
def longestCommonPrefix(strs):
    shortest_str = min(strs,key=len)

    return shortest_str

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))