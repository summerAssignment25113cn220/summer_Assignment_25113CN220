#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "Enter string: "; 
    cin >> str;

    bool seen[256] = {false};  // track seen characters
    cout << "without duplicates : ";

    for(int i = 0; str[i] != '\0'; i++){
        if(!seen[str[i]]){
            cout << str[i];
            seen[str[i]] = true;
        }
    }
    cout << endl;
}
// example : "programming" → "progamin"