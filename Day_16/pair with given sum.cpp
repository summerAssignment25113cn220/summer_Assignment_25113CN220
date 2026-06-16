#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "enter size: ";
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int target;
    cout << "enter sum: ";
    cin >> target;

    bool found = false;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(arr[i] + arr[j] == target){
                cout << "pair found: " << arr[i] << " + " << arr[j] << endl;
                found = true;
            }
        }
    }
    if(!found) cout << "no such pair" << endl;
}