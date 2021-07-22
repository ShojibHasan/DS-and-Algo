problems = int(input())
score =0
all_score =[]
for i in range(0,problems):
    marks = list(map(int,input().split()[:problems]))
    all_score.append(sum(marks))
    avg = sum(all_score)/problems
    maximum = max(all_score)
    minimum = min(all_score)

for i in range(problems):
    if all_score[i] == maximum:
        print("Participant1 = ",i+1)
    if all_score[i] == minimum:
        print("Participant3 = ",i+1)
    if all_score[i] != maximum and all_score[i] != minimum:
        print("Participant2 = ", i+1)


print(f"Participant1 scored top = {maximum} \nParticipant2 scored lowest  = {minimum} \nAvg score = {avg}")