def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime_number(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

n = int(input("Enter the value of n: "))
result = nth_prime_number(n)
print(f"The {n}th prime number is: {result}")