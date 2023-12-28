#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}


int isPrime(int num) {
    if (num < 2) {
        return 0; 
    }
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return 0; 
        }
    }
    return 1; 
}

int main() {
    int num;


    printf("Enter a number: ");
    scanf("%d", &num);

    while (num > 0) {
        int digit = num % 10;
        int fact = factorial(digit);

        printf("%d! = %d\n", digit, fact);

        if (isPrime(digit)) {
            printf("%d is a prime number\n", digit);
        } else {
            printf("%d is not a prime number\n", digit);
        }
        num /= 10;
    }

    return 0;
}
