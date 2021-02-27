n = int(input("enter a Number: "))
if not n%2==0:
    print("Opps")
elif n%2==0 and n>=6 and n<=10:
    print("Not Opps")
elif n%2==0 and n>=22 and n<=32:
    print("Opps")
elif n%2==0 and n>50:
    print("Opps")
