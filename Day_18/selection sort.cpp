#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "enter size : "; cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    for(int i = 0; i < n - 1; i++){
        int minIdx = i;
        for(int j = i + 1; j < n; j++){
            if(arr[j] < arr[minIdx]) minIdx = j;
        }
        // Swap
        int temp     = arr[minIdx];
        arr[minIdx]  = arr[i];
        arr[i]       = temp;
    }

    cout << "sorted array : ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}