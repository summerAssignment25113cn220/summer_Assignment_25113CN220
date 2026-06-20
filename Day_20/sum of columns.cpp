#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int r, c;
    cout << "enter rows and columns : "; 
    cin >> r >> c;
    
    int A[r][c];
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++) cin >> A[i][j];

    for(int j = 0; j < c; j++){       //  outer loop is for columns
        int sum = 0;
        for(int i = 0; i < r; i++) sum += A[i][j];
        cout << "Col " << j+1 << " sum = " << sum << endl;
    }
}