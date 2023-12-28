#include <stdio.h>

int main() {
    int n;

    printf("Enter the number: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i) {

        for (int num = i; num <= n; ++num) {
            printf("%d", num);
        }

        printf("\n");

        for (int space = 1; space <= i; ++space) {
            printf(" ");
        }
    }

    return 0;
}
