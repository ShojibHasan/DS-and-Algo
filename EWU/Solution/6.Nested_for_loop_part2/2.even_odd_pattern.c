#include <stdio.h>

int main() {
    int lines, limit;
    printf("Enter the number of lines: ");
    scanf("%d", &lines);

    printf("Enter the limit of numbers per line: ");
    scanf("%d", &limit);
    for (int i = 1; i <= lines; ++i) {
        int start = i;
        
        if (i % 2 != 0) {
            printf("Odd Line (%d): ", i);
            for (int j = 0; j < limit; ++j) {
                printf("%d", start);
                if (j < limit - 1) {
                    printf(",");
                }
                start += 2;
            }
        }
        else {
            printf("Even Line (%d): ", i);
            for (int j = 0; j < limit; ++j) {
                printf("%d", start);
                if (j < limit - 1) {
                    printf(",");
                }
                start += 2;
            }
        }
        printf("\n");
    }

    return 0;
}
