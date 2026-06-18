#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "enter size: "; cin >> n;

    int arr[n];
    cout << "enter SORTED array: ";
    for(int i = 0; i < n; i++) cin >> arr[i];

    int key;
    cout << "enter searching element : "; cin >> key;

    int low = 0, high = n - 1;
    bool found = false;

    while(low <= high){
        int mid = (low + high) / 2;
        if(arr[mid] == key){
            cout << "Found at index " << mid << endl;
            found = true;
            break;
        }
        else if(arr[mid] < key) low  = mid + 1;  // searches right half
        else                    high = mid - 1;  // searches left half
    }
    if(!found) cout << "not found" << endl;
}