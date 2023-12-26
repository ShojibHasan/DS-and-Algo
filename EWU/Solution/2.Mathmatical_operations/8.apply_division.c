#include <stdio.h>

int main() {
    int num1, num2;
    double result;

    printf("Enter num1: ");
    scanf("%d", &num1);

    printf("Enter num2: ");
    scanf("%d", &num2);

    if (num1 <= num2) {
        printf("num1 should be greater than num2.\n");
        return 1;  
    }

    result = (double)num1 / num2;
    printf("Output\n%.1lf point %.0lf\n", result, (result - (int)result) * 10);

    return 0;
}
