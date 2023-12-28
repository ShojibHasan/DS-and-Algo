#include <stdio.h>

int main() {
    int n;

    printf("Enter the number: ");
    scanf("%d", &n);

    int value = 1;
    for (int i = 1; i <= n; ++i) {
        int temp = value;
        for (int j = 1; j <= i; ++j) {
            printf("%d ", temp);
            temp += (n - j);
        }

        printf("\n");
        value++;
    }

    return 0;
}
