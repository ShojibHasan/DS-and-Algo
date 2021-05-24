station = int(input())
arr=[]
remain_passanger = 0
for i in range(station):
    exit, enter = map(int,input().split())
    remain_passanger += enter-exit

    arr.append(remain_passanger)
print(max(arr))