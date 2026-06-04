#include<bits/stdc++.h>
using namespace std;

int main(){
    int n; 
    cout << "Enter a number: ";
    cin >> n;

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
        sum = sum + pow(r, count);
        n = n / 10;            
    }
    
    if(sum == og){
        cout << "Armstrong number" << endl;
    }
    else{
        cout << "Not an Armstrong number" << endl;
    }
    
    return 0;
}