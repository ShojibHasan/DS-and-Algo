T = int(input())
for i in range(T):
    n = int(input())
    if n>10:
        n=n-10
        print("10 %i \n"%n)
    else:
        print("0 %i\n"%n)