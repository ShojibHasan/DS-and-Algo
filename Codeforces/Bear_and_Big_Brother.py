limak, bob = map(int,input().split())
iteration = 0
for i in range(1,bob+1):
    limak *= 3
    bob *=2
    iteration += 1

    if limak >bob:
        print(iteration)
        break
