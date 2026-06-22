#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter string : "; 
    cin >> str;

    char ch;
    cout << "enter character to find frequency : "; cin >> ch;

    int count = 0;
    for(int i = 0; str[i] != '\0'; i++){
        if(str[i] == ch) count++;
    }

    cout << ch << " appears " << count << " times in the strings" << endl;
}