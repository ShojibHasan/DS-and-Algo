# n = int(input())
# result=0
# for i in range(1,n+1):
#     print(i , " + ", end="")
#     result = result +i
# print("=",result)

i=1
sum = 0

while(i<4):
    while(i<3):
        sum = sum + i
        print(i , " + ", end="")
        i = i + 1
        if i == 3:
            sum = sum + i
            print(i,"=", sum)