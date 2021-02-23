num = int(input())
if num <=125:
    for i in range(num):
        a,b = list(map(int,input().split()))

        if 0<=a and a<=10 and 0<=b and b<=10:
            sum = a+b
            i = i+1
            print("Case %i:"%i,"%i"%sum)
