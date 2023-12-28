#include <stdio.h>

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);


    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (j == i) {
                printf("%d", i + 1);
            } else {
                printf("0");
            }
        }
        printf("\n");
    }

    return 0;
}
