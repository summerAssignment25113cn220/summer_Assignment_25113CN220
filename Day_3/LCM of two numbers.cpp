#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, m;
    cout << "Enter two numbers: ";
    cin >> n >> m;
    
    int lcm = max(n, m);  
    
    while(true){
        if(lcm % n == 0 && lcm % m == 0){  
            cout << "LCM is " << lcm << endl;
            break;
        }
        lcm++;  
    }
    return 0;
}