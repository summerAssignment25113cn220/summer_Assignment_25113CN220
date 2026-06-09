#include<bits/stdc++.h>
using namespace std;

int main(){
    int n; 
    cout << "number of rows's side : ";
    cin >> n;

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            // print * only on the border (first/last row or first/last column)
            if(i == 1 || i == n || j == 1 || j == n)
                cout << "* ";
            else
                cout << "  ";           // i have used one extra space, to make it look more of a square then a rectangle
        }
        cout << endl;
    }
}