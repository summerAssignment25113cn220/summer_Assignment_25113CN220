#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "Enter size: ";
    cin >> n;
    
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int key;
    cout << "Enter element: ";
    cin >> key;

    int count = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] == key) count++;
    }

    cout << key << " appears " << count << " times" << endl;
}