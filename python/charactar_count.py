# suppose you have given a string " Hello World"

# now find which character used how many times using python 


input_str = "Hello World"
count_value = {}
for i in input_str:
    if i in count_value:
        count_value[i] += 1
    else:
        count_value[i] = 1
print(count_value)

for i in input_str:
    if i in count_value:
        count_value[i] +=1
    else:
        count_value[i] =1