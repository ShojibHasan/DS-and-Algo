
def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    start,end = 0, len(s)-1
    s = list(s)
    while start < end :
        if s[start] not in vowels and s[end] not in vowels:
            start+=1
            end-=1
        elif s[start] not in vowels:
            start +=1
        elif s[end] not in vowels:
            end -=1
        else:
            s[start],s[end] = s[end], s[start]
            start+=1
            end-=1
    return ''.join(s)
            
a = reverseVowels("leetcode")
print(a)