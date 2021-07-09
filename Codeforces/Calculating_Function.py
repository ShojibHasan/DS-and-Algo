# n = int(input())
# plus_output = 0
# minus_output = 0
# for i in range(1,n+1):
#     if i%2 ==0:
#         plus_output = plus_output+1
#     elif i%2 !=0:
#         minus_output = minus_output-1
# if plus_output >= minus_output:
#     print(plus_output)
# else:
#     print(minus_output)

number = float(input())
number_dec = str(number-int(number))[1:]

print(f"number = {int(number)} number_dec= {number_dec}")
