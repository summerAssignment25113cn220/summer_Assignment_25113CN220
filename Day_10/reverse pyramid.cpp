#include<bits/stdc++.h>
using namespace std;

int main(){

    int n; 
    cout  << "enter number of rows : ";
    cin >> n;

    for(int i = n; i >= 1; i--){

        // prints space
        for(int j = 1; j <= n - i; j++)
            cout << " ";

        // prints star
        for(int j = 1; j <= 2*i - 1; j++)
            cout << "*";
        cout << endl;

    }
}
