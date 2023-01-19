from functools import lru_cache
import time



@lru_cache(maxsize=None)
def prime_number():
    lower = 1
    upper = 100000
    print("Prime numbers between", lower, "and", upper, "are:")
    prime_list=[]
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    
    return prime_list


def binary_search(item,list):
    low =0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        
        if guess==item:
            return mid,guess
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None

# def normal_search(item,list):
#     for i in list:
#         if i==item:
#             return i


start_time = time.perf_counter()
zz=binary_search(3191,prime_number())
print(len(prime_number()))
print(zz)
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

