#include <stdio.h>

int main() {
    int n;
    printf("Enter Number : ");
    scanf("%d", &n);

    printf("Prime numbers between 1 and %d are: ", n);

    for (int i = 2; i <= n; i++) {
        int p = 1; 

        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                p = 0; 
                break;
            }
        }

        if (p) {
            printf("%d\n", i);
        }
    }

    return 0;
}
