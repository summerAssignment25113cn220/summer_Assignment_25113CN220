#include<bits/stdc++.h>
using namespace std;

int main(){

    int n, m, p;
    cout << "enter size of array 1: "; 
    cin >> n;

    int arr1[n];
    for(int i = 0; i < n; i++) cin >> arr1[i];

    cout << "enter size of array 2: "; cin >> m;
    int arr2[m];
    for(int i = 0; i < m; i++) cin >> arr2[i];

    cout << "enter size of array 3: "; cin >> p;
    int arr3[p];
    for(int i = 0; i < p; i++) cin >> arr3[i];

    cout << "Common elements: ";
    for(int i = 0; i < n; i++){
        bool inArr2 = false, inArr3 = false;
        for(int j = 0; j < m; j++)
            if(arr1[i] == arr2[j]) inArr2 = true;
        for(int j = 0; j < p; j++)
            if(arr1[i] == arr3[j]) inArr3 = true;
        if(inArr2 && inArr3)
            cout << arr1[i] << " ";
    }
    cout << endl;
}