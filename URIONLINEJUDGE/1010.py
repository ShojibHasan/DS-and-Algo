A = input().split(" ")
B = input().split(" ")

code1,units1,price1 = A
code2,units2,price2 = B

total = (int(units1)*float(price1)) + (int(units2)* float(price2))
print("VALOR A PAGAR: R$ %.2f"%total)
