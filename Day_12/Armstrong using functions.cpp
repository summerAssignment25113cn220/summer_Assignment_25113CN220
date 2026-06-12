#include<bits/stdc++.h>
using namespace std;

bool arms(int n){
    int og = n;
    int count = 0;

    while(n > 0){
        n = n / 10;
        count++;
    }
    n = og;  
    int sum = 0;
    while(n > 0){
        int r = n % 10;        
        sum = sum + (int)round(pow(r, count));  // rounds of to the nearest integer (in case of floating number)
        n = n / 10;            
    }
    
    if(sum == og)return true;
    else{return false;}
}
int main(){
    int n;
    cout << "enter a number : ";
    cin >> n;

    int a = arms(n);
    if(a == true)cout << "armstrong number";
    else{cout << "not a armstrong number";}
}