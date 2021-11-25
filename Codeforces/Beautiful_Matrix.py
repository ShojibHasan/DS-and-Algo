index1 =0
index2 =0
value_list =[]
for i in range(5):
    word = list(map(int, input().split()))
    value_list.append(word)
    for j in range(0,5):
        if value_list[i][j] ==1:
            index1 = i-2
            index2 = j-2
print(abs(index1)+abs(index2))                                                          
