# a,b = 0,1
# while a<10:
#     print(a)
#     a,b = b, a+b

# def fibonacci(n):
#     if n ==1 or n==0:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(10))

def fibonacci(n):
    a,b = 0,1
    while a<n:
        print(a)
        a,b = b, a+b


fibonacci(10)