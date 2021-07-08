# from typing import AsyncGenerator


# def factorial1(n):
#     temp =1
#     for i in range(2,n+1):
#         temp = temp*i
#     return temp

# print(factorial1(4))

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))


# class StoryBook:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address


# book1= StoryBook('Shojib','24','Dhaka')
# print(book1.name)

# def outer(message):
#     print('Im outer function')

#     def inner():
#         print('Calling the inner function')
#         print(message)

#     return inner

# f = outer("Hello Workld")
# f()

def decoraor(original_func):
    print('In the decorator function \n')

    def wrapper():
        print(f'wrapper executed before {original_func.__name__}()')
        if 10>5:
            print('Yes it is true')

            return original_func() + 'extra string'

    return wrapper

