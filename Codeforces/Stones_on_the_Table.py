n = int(input())   
match = 0                    
color = list(input()[:n])
for i in range(len(color)-1):
    if color[i] == color[i+1]:
        match+=1
print(match)
    
