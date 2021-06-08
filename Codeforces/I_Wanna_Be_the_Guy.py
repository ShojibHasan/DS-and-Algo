n = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))
add_arr = x[1:] + y[1:]

level = set()
level.update(add_arr)


if len(level) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

