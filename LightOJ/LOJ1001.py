T = int(input())
for i in range(1,T+1):
    n = int(input())
    if n>10:
        n=n-10
        print("10 %i\n"%n-10)
    else:
        print("0 %i\n"%n)