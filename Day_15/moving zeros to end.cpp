#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout << "enter size: ";
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int pos = 0;                // for moving all non-zero elements to front of the array
    for(int i = 0; i < n; i++){
        if(arr[i] != 0){
            arr[pos] = arr[i];
            pos++;
        }
    }                   

    while(pos < n){             // // fill remaining positions with 0 
        arr[pos] = 0;
        pos++;
    }

    cout << "after moving zeroes: ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}