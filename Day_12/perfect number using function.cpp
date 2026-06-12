#include<bits/stdc++.h>
using namespace std;

bool perfect(int n){

    int sum = 0;
    for(int i = 1; i <= n/2; i++){
        if( n % i == 0 ){
            sum += i;
        }
    }
    if( sum == n ) return true;
    else{return false;}
}

int main (){

    int n;

    cout << "enter a number : ";
    cin >> n;

    int a = perfect(n);
    if(a==true)cout<<"perfect number";
    else{cout<<"Not a perfect number";}
    
}