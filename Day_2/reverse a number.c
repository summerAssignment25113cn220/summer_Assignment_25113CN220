#include <stdio.h>
int main()
{
    int n;
    printf("enter the a number :");
    scanf("%d",&n);
    int rev = 0,r;
    while(n>0)
    {   r=n%10;
        rev = rev*10 + r;
        n=n/10;
        
    }
    printf("reverse of the number is %d",rev);
    return 0;
}