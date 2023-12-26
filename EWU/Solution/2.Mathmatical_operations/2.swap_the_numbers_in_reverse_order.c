#include <stdio.h>

int main() {
    int num1, num2, num3, num4;

    printf("Enter four numbers (num1, num2, num3, num4): ");
    scanf("%d %d %d %d", &num1, &num2, &num3, &num4);

    num1 = num1 + num4;
    num4 = num1 - num4;
    num1 = num1 - num4;

    num2 = num2 + num3;
    num3 = num2 - num3;
    num2 = num2 - num3;

    printf("Swapped numbers in reverse order: %d %d %d %d\n", num1, num2, num3, num4);

    return 0;
}
