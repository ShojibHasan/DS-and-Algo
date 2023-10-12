
def miniMaxSum(arr):
    arr.sort()
    total_sum = sum(arr)
    min_sum = total_sum - arr[-1]
    max_sum = total_sum - arr[0]
    
    return(min_sum,max_sum)
        

arr = list(map(int, input().rstrip().split()))

a = miniMaxSum(arr)
print(a)