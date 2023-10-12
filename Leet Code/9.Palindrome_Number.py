# x = str(56565)
def isPalindrome(n):

    x = str(n)
    z = ""
    for i in range(len(x)-1,-1,-1):
        z += x[i]
    if x == z:
        return True
    else:
        return False
    
        
        
a = isPalindrome(-121)
print(a)