#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "enter size: "; 
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    // bubble sort but swap when arr[j] < arr[j+1]
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - i - 1; j++){
            if(arr[j] < arr[j + 1]){           // only change from ascending
                int temp   = arr[j];
                arr[j]     = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    cout << "descending order : ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}