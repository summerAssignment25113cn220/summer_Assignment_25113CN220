#include<bits/stdc++.h>
using namespace std;

int main(){

    int r, c;
    cout << "enter rows and columns : "; cin >> r >> c;
    int A[r][c];

    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++) cin >> A[i][j];

    for(int i = 0; i < r; i++){
        int sum = 0;
        for(int j = 0; j < c; j++) sum += A[i][j];
        cout << "Row " << i+1 << " sum = " << sum << endl;
    }
}