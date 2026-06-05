#include<bits/stdc++.h>
using namespace std;

int fact(int r){
    if(r==0)return 1;
    return r*fact(r-1);
}
//                                strong no. Example->   145 => 1! + 4! + 5! = 145                                   
int main (){
    
    int n;

    cout << "enter a number : ";
    cin >> n;

    int og = n;
    int sum = 0;
    
    while(n>0){
        int r = n % 10;
        sum += fact(r);
        n = n / 10;
    }

    if( sum == og ) cout << "strong number" << endl;
    else{cout<<"not a strong number";}
}