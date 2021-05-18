children, time = map(int,input().split())
children_name = list(input())
j=0
for i in range(time):
    j=1
    while children>j:
        if children_name[j-1]=="B" and children_name[j]=="G":
            children_name[j-1],children_name[j]=children_name[j],children_name[j-1]
            j+=1
        j+=1
print(''.join(children_name))
