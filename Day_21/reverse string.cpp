#include<bits/stdc++.h>
using namespace std;

int main(){
    
    char str[100];
    cout << "Enter a string: "; cin >> str;

    int len = 0;
    while(str[len] != '\0') len++;  // find length

    // swap from both ends
    int start = 0, end = len - 1;
    while(start < end){
        char temp  = str[start];
        str[start] = str[end];
        str[end]   = temp;
        start++;
        end--;
    }

    cout << "reversed string : " << str << endl;
}