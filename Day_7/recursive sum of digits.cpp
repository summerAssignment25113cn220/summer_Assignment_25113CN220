#include<bits/stdc++.h>
using namespace std; 

int sumD(int n){
    if(n == 0) return 0;
    return (n % 10) + sumD(n / 10);
}
int main(){

    int n; 
    cout << "enter a number : ";
    cin >> n;
    
    cout << "Sum = " << sumD(n) << endl;
}