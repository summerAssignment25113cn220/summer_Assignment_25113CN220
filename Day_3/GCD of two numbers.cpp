#include <bits/stdc++.h>
using namespace std;

int gcdf(int a,int b){
    int r;
    if(b == 0) return a;
    r = a % b;
    return gcdf(b,r);
    }

int main(){
    int n,m;
    cout << "enter two numbers : ";
    cin >> n >> m ;
    int out = gcdf(n,m);
    cout << "the GCD is " << out << endl;
return 0;
}