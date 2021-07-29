cgpa = float(input("Enter your CGPA: "))
income = int(input("Enter Family Income: "))

if cgpa >=3.00 and cgpa <= 3.50:
    if income <40000:
        print("scholarship: 50% ")
    elif income >=40001 and income <= 70000:
        print("scholarship: 30% ")
    elif income >=70001 and income <=100000:
        print("scholarship: 10% ")
    elif income > 100000:
        print("scholarship: 0% ")
    else:
        print("scholarship is 80%")

if cgpa >=3.50 and cgpa <=3.90:
    if income < 40000:
        print("scholarship: 60% ")