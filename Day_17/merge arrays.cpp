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

    cout << "merged array: ";
    for(int i = 0; i < n + m; i++) cout << merged[i] << " ";
    cout << endl;
}