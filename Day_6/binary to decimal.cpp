#include<bits/stdc++.h>
using namespace std;
int main(){
    string b;
    cout << "enter a binary code : ";
    cin >> b;
    int decimal = 0, power = 0;
    for(int i = b.length()-1; i >= 0; i--){
        if(b[i] == '1')
            decimal += pow(2, power);
        power++;
    }
    cout << "Decimal = " << decimal << endl;
}