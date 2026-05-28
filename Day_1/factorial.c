#include <stdio.h>
int main()
{
    int n;
    printf("enter the a number :");
    scanf("%d",&n);
    int fact=1;
    for (int i = 1; i <= n; i++)
    {
        fact*=i;
    }
    printf("the sum of N natural numbers is %d",fact);
    return 0;
}