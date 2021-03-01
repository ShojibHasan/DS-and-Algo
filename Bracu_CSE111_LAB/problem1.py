string = input("Enter the String : ")

lower_case_count =0
upper_case_count = 0

for i in string:
    if(i.islower()):
        lower_case_count = lower_case_count+1
    elif(i.isupper()):
        upper_case_count = upper_case_count+1

if upper_case_count>lower_case_count:
    print(string.upper())
else:
    print(string.lower())
    