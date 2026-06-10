#include<bits/stdc++.h>
using namespace std;

int main(){

    int n; 
    cout << "enter number of rows : ";
    cin >> n;

    for(int i = 1; i <= n; i++){

        // prints space
        for(int j = 1; j <= n - i; j++)
            cout << " ";

        // prints characters going up-> A B C...
        for(int j = 1; j <= i; j++)
            cout << (char)('A' + j - 1);

        // print characters going down-> ...C B A
        for(int j = i - 1; j >= 1; j--)
            cout << (char)('A' + j - 1);
        cout << endl;

    }
}