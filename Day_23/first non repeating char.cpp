#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter string : "; 
    cin >> str;

    int len = 0;
    while(str[len] != '\0') len++;

    char result = '\0';
    for(int i = 0; i < len; i++){
        int count = 0;
        for(int j = 0; j < len; j++){
            if(str[i] == str[j]) count++;
        }
        if(count == 1){        // appears only once
            result = str[i];
            break;
        }
    }

    if(result) cout << "first non-repeating : " << result << endl;
    else       cout << "No non-repeating character" << endl;
}