#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cout << "enter size (n x n) : "; cin >> n;
    int A[n][n];

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++) cin >> A[i][j];

    int sum = 0;
    for(int i = 0; i < n; i++)
        sum += A[i][i];  // diagonal elements: A[0][0], A[1][1], A[2][2]...

    cout << "diagonal sum = " << sum << endl;
}