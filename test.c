#include <stdio.h>
int main() {
   int i, j, rows;
   printf("Enter the number of line: ");
   scanf("%d", &rows);
   for (i = 1; i <= rows; ++i) {
    //   printf("%d",i); 1,2,3,4
      for (j = 1; j <= i; ++j) {
         printf("* ");
      }
      printf("\n");
   }
   return 0;
}