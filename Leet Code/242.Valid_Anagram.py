from collections import defaultdict
def isAngama():
    a = "anagram"
    b = "nagaram"


    hash = defaultdict(int)
    for c in a:
        hash[c] += 1
    for c in b:
        hash[c]-=1
    
    for c,v in hash.items():
        if v != 0:
            return False
    return True

print(isAngama())