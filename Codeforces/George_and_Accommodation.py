total_room = int(input())
move_in =0
for i in range(total_room):
    existing, capacity = map(int,input().split())
    if capacity-existing >=2:
        move_in +=1
print(move_in)
