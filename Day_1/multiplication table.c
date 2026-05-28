#include<stdio.h>
int main(){
    int n;
    printf("enter a number");
    scanf("%d",&n);
    int p;
for(int i=1; i<=10; i++){
    p=n*i;
    printf("%d x %d = %d\n",n,i,p);
}
    return 0;
}