#include <stdio.h>
int main()
{
    int n;
    printf("enter the a number :");
    scanf("%d",&n);
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    printf("the sum of N natural numbers is %d", sum);
    return 0;
}