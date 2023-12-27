#include<stdio.h>

int main() {
    
    int number;
    int finalnumber;

    printf("Enter number : ");

    scanf("%d",&finalnumber);

    int factorial = 1;

    for (number=1; number<=finalnumber; number++) {
        printf("Factorial of %d is : ",number);
        factorial *= number;
        printf("%d \n",factorial);
    }

    return 0;
}