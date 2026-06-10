#include<bits/stdc++.h>
using namespace std;

int main(){

    int n; 
    cout << "enter number of rows : ";
    cin >> n;

    for(int i = 1; i <= n; i++){
        
        // prints spaces first
        for(int j = 1; j <= n - i; j++)
            cout << " ";

        // print star in odd numbers like  1 star , 3 star , 5 star in a row
        for(int j = 1; j <= 2*i - 1; j++)
            cout << "*";
        cout << endl;

    }
}
