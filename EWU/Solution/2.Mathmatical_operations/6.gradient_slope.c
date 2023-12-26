#include <stdio.h>

int main() {
    double x1, y1, x2, y2, s;

    printf("First number, x1  = ");
    scanf("%lf", &x1);

    printf("Second number, y1 = ");
    scanf("%lf", &y1);

    printf("Third number, x2 = ");
    scanf("%lf", &x2);

    printf("Forth number, y2 = ");
    scanf("%lf", &y2);

    s = (y2 - y1) / (x2 - x1);

    printf("Gradient slope of straight line, M = %.4lf\n", s);

    return 0;
}
