number = input()

# list_luckyNumber = list(map(int, str(lucky_number)))
lucky_number =0
for i in range(len(number)):
    if number[i] =='4' or number[i]=='7':
        lucky_number +=1
        

if lucky_number==4 or lucky_number==7:
    print("YES")
else:
    print("NO")