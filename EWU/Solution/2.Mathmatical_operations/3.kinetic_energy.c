#include <stdio.h>
#include <math.h>

int main() {
    double v, m, k;

    printf("Enter velocity: ");
    scanf("%lf", &v);

    printf("Enter mass: ");
    scanf("%lf", &m);

    k = 0.5 * m * pow(v, 2);

    printf("Kinetic Energy = %.2lf kg m^2/s^2 \n", k);

    return 0;
}
