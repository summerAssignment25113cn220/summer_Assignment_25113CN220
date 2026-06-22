#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter string : "; 
    cin >> str;

    int len = 0;
    while(str[len] != '\0') len++;

    bool isP = true;
    int start = 0, end = len - 1;
    while(start < end){
        if(str[start] != str[end]){
            isP = false;
            break;
        }
        start++;
        end--;
    }

    if(isP) cout << "Palindrome" << endl;
    else        cout << "Not Palindrome" << endl;
}