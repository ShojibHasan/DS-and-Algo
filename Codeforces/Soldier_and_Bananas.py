k,n,w = map(int,input().split())
total_price =0
for i in range(1,w+1):
    total_price += i*k
money_borrow = total_price-n
if money_borrow<0:
    print(0)
else:
    print(money_borrow)

