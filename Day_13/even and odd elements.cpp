#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "Enter size: ";
    cin >> n;
    
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int even = 0, odd = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] % 2 == 0) even++;
        else odd++;
    }

    cout << "Even count = " << even << endl;
    cout << "Odd count  = " << odd  << endl;
}