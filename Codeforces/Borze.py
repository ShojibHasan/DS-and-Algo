
numeric_notation = input()
num = 0
lenghth =''
while num<len(numeric_notation):
    if numeric_notation[num]=='.':
        lenghth+=str(0)
        num+=1
        continue
    elif numeric_notation[num]=='-' and numeric_notation[num+1]=='.':
        lenghth+= str(1)
        num+=2
        continue
    elif numeric_notation[num]=='-' and numeric_notation[num+1]=='-':
        lenghth+=str(2)
        num+=2
        continue
    num+=1
print(lenghth)
