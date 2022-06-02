def slow_solution(arr):
    max_prodcut = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            max_prodcut = max(max_prodcut,arr[i]*arr[j])
    return max_prodcut




def fast_solution(arr):
    index_one = -1
    for i in range(len(arr)):
        if index_one == -1 or arr[i] > arr[index_one]:
            index_one = i
    
    index_two = -1
    for j in range(len(arr)):
        if j != index_one and (index_two == -1 or arr[j]>arr[index_two]):
            index_two = j
    
    return arr[index_one] * arr[index_two]



import random
def stres_test(n,m):
    while True:
        n = random.randint(10,n)
        print(n)
        a = [random.randint(0,m) for i in range(n)]
        print(a)
        res_one = slow_solution(a)
        res_two = fast_solution(a)

        if res_one == res_two:
            print('Both are OK!!')
        else:
            print('Something went wrong .. ops !!',res_one,res_two)
            break





n = 100
m = 10000000
stres_test(n,m)