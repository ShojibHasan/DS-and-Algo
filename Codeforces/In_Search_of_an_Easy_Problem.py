n = int(input())
problems = list(map(int,input().split()[:n]))

if 1 in problems:
    output = 'HARD'
else:
    output = 'EASY'
print(output)