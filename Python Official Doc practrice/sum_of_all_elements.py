def sum_of_elements(arra,number):
    s =0
    for i in range(0,number):
        s = s+arra[i]
    return s

arra = [10,2,33,10,3,4,5]
number = len(arra)
print(sum_of_elements(arra,number))
