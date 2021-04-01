#Remove The Duplicate Elements From a List/Array

arr = [11,11,22,33,22,555,44,33,4564,676,11]
unique_values =[]

for i in arr:
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)