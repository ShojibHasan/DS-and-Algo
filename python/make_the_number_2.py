
def make_the_number(array,length_array,number):
    left =0
    right = length_array-1
    for i in range(length_array):
        if array[left]+array[right]==number:
            return "paisi tomare chando: ", (left, right)
        elif array[left]+ array[right] >=number:
            right -=1
        elif array[left]+array[right] <=number:
            left +=1

arrary = [3,2,4]
number = 6
length_array = len(arrary)
print(make_the_number(arrary,length_array,number))