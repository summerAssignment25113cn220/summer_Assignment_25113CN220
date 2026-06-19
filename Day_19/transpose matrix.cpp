#include<bits/stdc++.h>
using namespace std;

int main(){

    int r, c;
    cout << "enter rows and columns : "; cin >> r >> c;
    int A[r][c], T[c][r];

    cout << "enter matrix :\n";
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++) cin >> A[i][j];

    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            T[j][i] = A[i][j];

    cout << "transposed matrix :\n";
    for(int i = 0; i < c; i++){
        for(int j = 0; j < r; j++) cout << T[i][j] << " ";
        cout << endl;
    }
}