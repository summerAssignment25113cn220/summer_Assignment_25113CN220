#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout << "Enter size: ";
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int k;
    cout << "rotate by: ";
    cin >> k;

    for(int r = 0; r < k; r++){
        int first = arr[0];
        for(int i = 0; i < n - 1; i++)
            arr[i] = arr[i + 1];
        arr[n - 1] = first;
    }

    cout << "resulting array : ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}