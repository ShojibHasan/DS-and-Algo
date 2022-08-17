text = 'MOM'

i =0
j = len(text)-1

for i in range(j):
    if text[i] == text[j]:
        i+=1
        j-=1
        
        print("valid Palindrom")