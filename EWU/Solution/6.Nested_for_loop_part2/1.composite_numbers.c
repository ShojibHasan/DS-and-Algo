#include <stdio.h>

int main() {
    int n;

    printf("Enter Number = ");
    scanf("%d", &n);
    
    printf("Composite numbers are :\n");
    
    for (int i = 2; i <= n; ++i) {
        int c = 0; 
        
        for (int j = 2; j <= i / 2; ++j) {
            if (i % j == 0) {
                c = 1;
                break;
            }
        }

        if (c) {
            printf("%d ", i);
        }
    }

    return 0;
}
