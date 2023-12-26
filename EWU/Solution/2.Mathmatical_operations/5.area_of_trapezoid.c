#include <stdio.h>

int main() {
    double height, base1, base2, area;

    printf("Enter height: ");
    scanf("%lf", &height);

    printf("Enter length of base 1: ");
    scanf("%lf", &base1);

    printf("Enter length of base 2: ");
    scanf("%lf", &base2);

    area = 0.5 * (base1 + base2) * height;

    printf("Area of trapezoid: %.4lf\n", area);

    return 0;
}
