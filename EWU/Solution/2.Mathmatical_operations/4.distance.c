#include <stdio.h>

int main() {
    double a, m,s, d;

    printf("Enter speed : ");
    scanf("%lf", &a);

    printf("Enter time(minutes) = ");
    scanf("%lf", &m);
    
    printf("Enter time(seconds) = ");
    scanf("%lf", &s);
    
    s += m*60;
    m = s/60;

    d = a * m;

    printf("Distance: %.2lf km\n", d);

    return 0;
}
