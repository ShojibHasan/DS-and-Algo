# Python program to display all the prime numbers within an interval

lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")
prime_list=[]
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime_list.append(num)
           print(num)
        