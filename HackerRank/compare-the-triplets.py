def compareTriplets(a, b):
    alice=0
    bob =0
    for i in range(0,3):
        if (a[i]>b[i]):
            alice +=1
        
        elif (a[i]<b[i]):
            bob = bob+1
    result= [alice,bob]
    return " ".join(map(str,result))


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)
print(result)
