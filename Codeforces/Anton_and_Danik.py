played_games = int(input())
winner = input()[:played_games]
anton = 0
danik = 0
for i in range(len(winner)):
    if winner[i]=='A':
        anton += 1
    elif winner[i] =='D':
        danik += 1
if anton > danik:
    print("Anton")
elif danik>anton:
    print("Danik")
else:
    print("Friendship")