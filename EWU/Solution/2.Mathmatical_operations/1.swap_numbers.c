#include <stdio.h>

int main() {
    int a,b;
    printf("Enter Number One: ");
    scanf("%d",&a);
    printf("Enter Number Two: ");
    scanf("%d",&b);
    a= a+b;
    b = a-b;
    a = a-b;
    
    printf("Swaped Value One : %d\n",a);
    printf("Swaped Value Two : %d",b);

    return 0;
}
