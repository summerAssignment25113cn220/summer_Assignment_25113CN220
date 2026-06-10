#include<bits/stdc++.h>
using namespace std;

int main(){

    int n; 
    cout << "enter number of rows : ";
    cin >> n;
    
    for(int i = 1; i <= n; i++){

        // print space
        for(int j = 1; j <= n - i; j++)
            cout << " ";

        // print numbers going up-> 1 2 3...i
        for(int j = 1; j <= i; j++)
            cout << j;
            
        // print numbers going down-> i-1...1
        for(int j = i - 1; j >= 1; j--)
            cout << j;
        cout << endl;

    }
}