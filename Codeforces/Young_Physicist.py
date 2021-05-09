def equilibrium(coordinates):
    value1 =0
    value2=0
    value3 =0
    for i in range(coordinates):
        x,y,z = map(int,input().split())

        value1 +=x
        value2 +=y
        value3 +=z

    if value1==value2==value3==0:
        print("YES")
    else:
        print("NO")

coordinates = int(input())
equilibrium(coordinates)
