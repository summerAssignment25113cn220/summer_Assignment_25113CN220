#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "Enter size (n x n): "; cin >> n;
    int A[n][n];

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++) cin >> A[i][j];

    bool symmetric = true;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(A[i][j] != A[j][i]){
                symmetric = false;
                break;
            }
        }
    }

    if(symmetric) cout << "Matrix is Symmetric" << endl;
    else          cout << "Matrix is NOT Symmetric" << endl;
}