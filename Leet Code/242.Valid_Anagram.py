from collections import defaultdict
def isAngama(a,b):

    hash = defaultdict(int)
    for c in a:
        hash[c] += 1
    for c in b:
        hash[c]-=1
    
    for c,v in hash.items():
        if v != 0:
            return False
    return True

a = "anagram"
b = "nagaram"
print(isAngama(a,b))