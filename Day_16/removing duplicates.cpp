#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cout << "enter size: ";
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    cout << "after removing duplicates: ";
    for(int i = 0; i < n; i++){
        bool isDup = false;
        for(int j = 0; j < i; j++){
            if(arr[i] == arr[j]){
                isDup = true;
                break;
            }
        }
        if(!isDup) cout << arr[i] << " ";
    }
    cout << endl;
}