#include <stdio.h>
int main()
{
    int n;
    printf("enter the a number :");
    scanf("%d",&n);
    int sum = 0;
    int r;
    while(n>0)
    {   r=n%10;
        sum+=r;
        n=n/10;
        
    }
    printf("sum of the digits is %d",sum);
    return 0;
}