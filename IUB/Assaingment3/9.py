a,b,c = input().split()

if (a + b <= c) or (a + c <= b) or (b + c <= a) :
    print("Right triangle")
else:
    print("Not a right triangle ")