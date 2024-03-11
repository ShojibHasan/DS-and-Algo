# suppose you have given a string " Hello World"

# now find which character used how many times using python 


input_string = "Hello World"
char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] =1


for char,count in char_count.items():
    print(f"character '{char}' occurs {count} times") 