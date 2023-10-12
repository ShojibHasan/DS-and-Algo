def numJewelsInStones(jewels,stones):
    a = 0
    for i in stones:
        if i in jewels:
            a+=1
    return a
    
    
a = numJewelsInStones("aA","aAAbbbb")
print(a)