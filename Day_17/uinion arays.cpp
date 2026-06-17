#include<bits/stdc++.h>
using namespace std;

int main(){

    int n, m;
    cout << "enter size of array 1: ";
    cin >> n;

    int arr1[n];
    for(int i = 0; i < n; i++) cin >> arr1[i];

    cout << "enter size of array 2: ";
    cin >> m;

    int arr2[m];
    for(int i = 0; i < m; i++) cin >> arr2[i];

    int merged[n + m];
    for(int i = 0; i < n; i++)     merged[i]     = arr1[i];
    for(int i = 0; i < m; i++)     merged[n + i] = arr2[i];
    int total = n + m;

    cout << "Union: ";
    for(int i = 0; i < total; i++){
        bool isDup = false;
        for(int j = 0; j < i; j++){
            if(merged[i] == merged[j]){ isDup = true; break; }
        }
        if(!isDup) cout << merged[i] << " ";
    }
    cout << endl;
}