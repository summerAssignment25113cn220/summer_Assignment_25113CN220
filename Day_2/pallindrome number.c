#include <stdio.h>
int main()
{
    int n, rev = 0, r;
    int original;
    printf("enter a number: ");
    scanf("%d", &n);
    original = n;        // save original number
    while(n > 0)
    {
        r = n % 10;
        rev = rev * 10 + r;
        n = n / 10;  
    }
    if(original == rev)
        printf("%d is a palindrome", original);
    else
        printf("%d is not a palindrome", original);
    return 0;
}