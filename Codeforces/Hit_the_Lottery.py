n  = int(input())
count=0
money = [100,20,10,5,1]
for i in range(5):
    count +=n//money[i]
    n =n%money[i]
print(count)