import decimal

n = int(input())
drinks = list(map(int,input().split()[:n]))
Sum = sum(drinks)

print(round(Sum/n,12))

# 66.66666666666667
# 66.666666666667