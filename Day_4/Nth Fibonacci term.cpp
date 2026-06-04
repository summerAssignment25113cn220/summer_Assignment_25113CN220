#include<bits/stdc++.h>
using namespace std;

int fibo(int n){
    if(n==1 || n==2)return 1;
    return fibo(n-1)+fibo(n-2);
}
int main(){
    int n;
    cout << "enter the term number : ";
    cin >> n;
    
    cout <<"the "<<n<<"th term is " << fibo(n) << endl;
    return 0;
}