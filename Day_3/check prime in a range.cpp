#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cout << "enter a number: ";
    cin >> n;

    for (int i = 2; i <= n; i++)
    {
        int flag = 1;  // assume prime
        for (int j = 2; j <= i / 2; j++)
        {
            if (i % j == 0)
            {
                flag = 0;  // not prime
                break;
            }
        }
        if (flag == 1)
            cout << i << " ";
    }
    return 0;
}
