fib1 = 0
fib2 = 1
result =0
for num in range(1,10):
    print(result,end =" ")
    fib1 = fib2
    fib2 = result   
    result = fib1 + fib2
 
    

# def fibonacci(num):
#     num1 = 0
#     num2 = 1
#     series = 0
#     for i in range(1,num):
#         print(series, end=' ')
#         num1 = num2
#         num2 = series
#         series = num1 + num2
 

# num = 10
# fibonacci(num)