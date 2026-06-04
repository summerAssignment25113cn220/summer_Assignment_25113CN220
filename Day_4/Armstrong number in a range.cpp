#include<bits/stdc++.h>
using namespace std;

int main(){
    int n; 
    cout << "Enter the range n : ";
    cin >> n;

    for(int num = 1; num <= n; num++){
        int original = num;
        int temp = num;
        int count = 0;

        while(temp > 0){
            temp = temp / 10;
            count++;
        }
        temp = original;
        int sum = 0;
        while(temp > 0){
            int digit = temp % 10;
            sum = sum + pow(digit, count);
            temp = temp / 10;
        }
        if(sum == original){
            cout << original << " ";
        }
    }
    
    cout << endl;
    return 0;
}