#include <bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cout << "enter a number : ";
    cin >> n;

    int flag = 1;  // assume prime
        for (int j = 2; j <= n / 2; j++)
        {
            if (n % j == 0)
            {
                flag = 0;  // not prime
                break;
            }
        }
        if (flag == 1)
            cout <<" it is prime";
        else 
            cout << "not a prime";
    return 0;
}