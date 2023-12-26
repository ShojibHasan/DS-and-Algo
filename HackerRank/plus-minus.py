def plusMinus(arr):
    array_length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i >0:
            positive += 1
        if i<0:
            negative += 1
        if i==0:
            zero += 1
    print("%0.6f"%(positive/array_length))
    print("%0.6f"%(negative/array_length))
    print("%0.6f"%(zero/array_length))
    
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)