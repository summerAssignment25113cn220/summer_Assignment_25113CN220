#include<bits/stdc++.h>
using namespace std;

int max(int a, int b){
    
    if(a > b) return a;
    else return b;
}

int main(){

    int a, b;
    cout << "enter two numbers: ";
    cin >> a >> b;

    cout << "Maximum = " << max(a, b) << endl;
}