x = input("Enter the String: ")
w2 = ''
inBetween = False

for i in x:
    if i.isupper():
        if not inBetween:
            inBetween = True
            continue
        else:
            inBetween = False
            break
    if inBetween:
        w2+= i

if w2:
    print(w2)
else:
    print("BLANK")