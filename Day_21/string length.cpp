#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter a string: "; cin >> str;

    int count = 0;
    while(str[count] != '\0'){  // '\0' is end of string
        count++;
    }

    cout << "length = " << count << endl;
}