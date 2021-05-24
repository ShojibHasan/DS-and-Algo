
words  = input()
upper_count =0
lower_count = 0

for i in range(len(words)):
    if words[i].isupper():
        upper_count += 1
    elif words[i].islower():
        lower_count +=1
        
if upper_count>lower_count:
    print(words.upper())
elif lower_count>upper_count:
    print(words.lower())
else:
    print(words.lower())


