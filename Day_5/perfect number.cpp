#include<bits/stdc++.h>
using namespace std;

int main (){

    int n;

    cout << "enter a number : ";
    cin >> n;

    int sum = 0;
    for(int i = 1; i <= n/2; i++){
        if( n % i == 0 ){
            sum += i;
        }
    }
    if( sum == n ) cout << "perfect number" << endl;
    else{cout<<"not a perfect number";}
}
//     if the sum of all the factors of the given number is equal to the number itself.