#include <stdio.h>

int main() {
    int year, month, week, day;
    int hours;

    printf("Enter years: ");
    scanf("%d", &year);

    printf("Enter months: ");
    scanf("%d", &month);

    printf("Enter weeks: ");
    scanf("%d", &week);

    printf("Enter days: ");
    scanf("%d", &day);

    hours = (year * 365.25 * 24) + (month * 30 * 24) + (week * 7 * 24) + (day * 24);

    printf("Total hours is: %d\n", hours);

    return 0;
}
