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

    cout << "intersection: ";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(arr1[i] == arr2[j]){
                cout << arr1[i] << " ";
                break;
            }
        }
    }
    cout << endl;
}