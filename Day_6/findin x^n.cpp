#include<bits/stdc++.h>
using namespace std;
int main(){
    int x, n, result = 1;
    cout << "enter a number : ";
    cin >> x;
    cout << "enter its power : ";
    cin  >> n;
    for(int i = 0; i < n; i++)
        result = result * x;
    cout << x << "^" << n << " = " << result << endl;
}