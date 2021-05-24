person, height = map(int,input().split())
data = list(map(int,input().split()[:person]))
score2 = 0
score1 =0
for i in range(len(data)):
    if data[i] >height:
        score2 += 2
    elif data[i] <= height:
        score1 +=1

print(score1+score2)