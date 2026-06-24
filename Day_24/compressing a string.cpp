#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter string : "; cin >> str;

    cout << "Compressed: "; // "aaabbbcc" → "a3b3c2"

    int i = 0;
    while(str[i] != '\0'){
        char ch = str[i];
        int count = 0;
        while(str[i] == ch){
            count++;
            i++;
        }
        cout << ch << count;
    }
    cout << endl;
}