#include <stdio.h>

int main() {
    int lines;
    printf("Enter the line limit: ");
    scanf("%d", &lines);


    for (int i = 1; i <= lines; ++i) {

        for (int j = 1; j < i; ++j) {
            printf("  ");
        }
        for (int j = i; j <= lines; ++j) {
            printf("%d ", i);
        }

        printf("\n");
    }

    return 0;
}
