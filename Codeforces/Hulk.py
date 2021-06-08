love = "I love "
hate = "I hate "
line = ""

layer = int(input())

line = hate
for i in range(2,layer+1):
    line+= "that "
    if i % 2 ==0:
        line += love
    else:
        line += hate
line += "it "

print(line)