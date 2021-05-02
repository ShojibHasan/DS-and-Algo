n = int(input("Enter the Problem: "))
# for i in range(1,11):
#     multiplication = i*n
#     print(n,"X",i,"=",multiplication)
print(str([x*n for x in range(1,11)])[1:-1])
