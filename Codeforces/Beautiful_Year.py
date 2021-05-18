# year = int(input())
# while True:
#     year = year+1
#     a = year //1000
#     b = (year//100)%10
#     c = (year//10)%10
#     d = year%10
#     if (a!=b and a!=c and c!=d and b!=c and b!=d and c!=d and a!=d):
#         break
# print(year)

def solve(year):
    while True:
        year = str(int(year)+1)
        set_year = set(year)
        if(len(set(year))==4):
            return year

print(solve(input()))