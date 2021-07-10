data1 = input()
data2 = input()
value1 =''
# value2 =''
# value3 = ''
for i in range(len(data1)):
    if data1[i] =='1' and data2[i]=='0':
        value1 += '1'
    elif data1[i] =='0' and data2[i]=='1':
        value1 +='1'


    if data1[i] =='0' and data2[i]=='0':
        value1 +='0'
    if data1[i] == '1' and data2[i]=='1':
        value1 += '0'
print(value1)