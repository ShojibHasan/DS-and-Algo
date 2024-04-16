# a = [12, 34, 56, 10, 3, 9, 11, 21, 12]
# target=33


def target_value(a,target):
    start = 0
    end = len(a) - 1
    a = sorted(a)
    while start < end:

        if a[start] + a[end]==target:
            return a[start],a[end]
        else:
            if a[end] > target:
                end -=1
            if a[start] < target:
                start +=1

a = [2,7,11,15]
target = 9
print(target_value(a,target))