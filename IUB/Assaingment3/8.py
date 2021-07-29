x = int(input())
y = int(input())

if x<0 and y<=0:
    print("3nd quadrant")
elif x<0 and y==0:
    print("x-axsis ")
elif x==0 and y==0 :
    print("Origin ")
elif x == 0 and y>0:
    print("y-Axis")
elif x > 0 and y>0:
    print("1st quadrant")
