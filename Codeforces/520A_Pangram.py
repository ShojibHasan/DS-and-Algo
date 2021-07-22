n = int(input())
string = input()

for i in range(n):
    if ord(string[i]) <=65 and ord(string[i]) >= 90 or ord(string[i]) <=97 and ord(string[i]) >=122:
        print("YES")
    else:
        print("NO")