#include<bits/stdc++.h>
using namespace std;

int main(){

    int r, c;
    cout << "enter rows and columns : "; cin >> r >> c;

    int A[r][c], B[r][c], C[r][c];

    cout << "enter matrix A:\n";
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++) cin >> A[i][j];

    cout << "enter matrix B:\n";
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++) cin >> B[i][j];

    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            C[i][j] = A[i][j] + B[i][j];

    cout << "resulting matrix on addition :\n";
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++) cout << C[i][j] << " ";
        cout << endl;
    }
}