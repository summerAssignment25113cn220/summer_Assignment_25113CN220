#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cout << "enter a decimal number : ";
    cin >> n;
    int og = n;
    string binary = "";
    while(n > 0){
        binary = to_string(n % 2) + binary;
        n = n / 2;
    }
    cout << og << " in binary = " << binary << endl;
}