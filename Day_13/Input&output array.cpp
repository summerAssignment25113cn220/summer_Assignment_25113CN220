#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "Enter size of array: ";
    cin >> n;

    int arr[n];
    cout << "enter elements : ";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Array: ";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}