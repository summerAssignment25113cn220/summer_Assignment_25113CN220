#include<bits/stdc++.h>
using namespace std;

int main (){
    
    int n;

    cout << "enter a number : ";
    cin >> n;

    cout << "the factors of "<<n<< "are : ";
    for(int i = 1; i <= n/2; i++){
        if( n % i == 0 )cout << i <<" ";
    }
    cout << n;
}