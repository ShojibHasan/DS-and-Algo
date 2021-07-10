values = input()
final_values = values.translate({ ord(c): None for c in ".,{} " })
data = set()
total =0
for i in range(len(final_values)):
    if final_values[i] not in data:
        total +=1
    data.add(final_values[i])
print(total)

# https://careerkarma.com/blog/python-remove-character-from-string/