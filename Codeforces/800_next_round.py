def next_round(n,k):
    scores_input = input().split()
    passed = 0
    for i in range(n):
        if int(scores_input[i]) >= int(scores_input[k-1]) and int(scores_input[i]) !=0 :
            passed = passed+1
    print(passed)

n, k = map(int,input().split())

next_round(n,k)

# n =8
# k =5