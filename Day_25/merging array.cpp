#include<bits/stdc++.h>
using namespace std;

int main(){

    int n, m;
    cout << "Enter size of sorted array 1: "; cin >> n;
    int arr1[n];
    for(int i = 0; i < n; i++) cin >> arr1[i];

    cout << "Enter size of sorted array 2: "; cin >> m;
    int arr2[m];
    for(int i = 0; i < m; i++) cin >> arr2[i];

    int merged[n + m];
    int i = 0, j = 0, k = 0;

    // Pick smaller element from both arrays
    while(i < n && j < m){
        if(arr1[i] < arr2[j]) merged[k++] = arr1[i++];
        else                   merged[k++] = arr2[j++];
    }
    while(i < n) merged[k++] = arr1[i++];  // remaining
    while(j < m) merged[k++] = arr2[j++];  // remaining

    cout << "Merged sorted : ";
    for(int x = 0; x < n + m; x++) cout << merged[x] << " ";
    cout << endl;
}