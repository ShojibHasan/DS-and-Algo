#include <stdio.h>

int main() {
    int n, m, count = 0;

    printf("Enter the starting year = ");
    scanf("%d", &n);

    printf("Enter the ending year = ");
    scanf("%d", &m);

    printf("Leap years between %d and %d are: ", n, m);

    for (int year = n; year <= m; year++) {
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            printf("%d ", year);
            count++;
        }
    }

    if (count > 0) {
        printf("\nTotal leap years: %d\n", count);
    } else {
        printf("\nNo leap year found.\n");
    }

    return 0;
}
