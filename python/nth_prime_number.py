def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime_number(n):
    count = 0
    num = 2
    list_of_primes = []
    while count < n:
        if is_prime(num):
            count += 1
            list_of_primes.append(num)
        num += 1
    return num

n = int(input("Enter the value of n: "))
result = nth_prime_number(n)
print(f"The {n}th prime number is: {result}")