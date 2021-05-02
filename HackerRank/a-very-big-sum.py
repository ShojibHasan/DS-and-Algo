def aVeryBigSum(ar):
    bigsum = 0
    for i in range(len(ar)):
        bigsum += ar[i]
    return bigsum


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(result)