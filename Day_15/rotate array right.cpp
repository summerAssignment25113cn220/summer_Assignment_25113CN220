#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout << "enter size: ";
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int k;
    cout << "rotate by: ";
    cin >> k;

    for(int r = 0; r < k; r++){
        int last = arr[n - 1];
        for(int i = n - 1; i > 0; i--)
            arr[i] = arr[i - 1];
        arr[0] = last;
    }

    cout << "resulting array : ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}