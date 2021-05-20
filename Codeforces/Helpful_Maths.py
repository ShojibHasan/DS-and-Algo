addition_operation = input()
num=0
numbers=''
final_number=''
while num< len(addition_operation):
    numbers += str(addition_operation[num])
    num+=2
numbers = '+'.join(sorted(numbers))
print(numbers)