number = input("Enter a number")
sum =1
temp = number
while temp >0:
    digit = temp
    sum += digit **2
    temp %=10

while number==sum:
    print(number,"is an Aramstrong number")
else:
    print(number,"is not an Aramstrong number")
