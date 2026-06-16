#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout << "enter n (array has 1 to n number adn one missing): ";
    cin >> n;

    int arr[n-1];
    for(int i = 0; i < n-1; i++) cin >> arr[i];

    int expected = n * (n + 1) / 2;
    int actual = 0;
    for(int i = 0; i < n-1; i++) actual += arr[i];

    cout << "missing number : " << expected - actual << endl;
}