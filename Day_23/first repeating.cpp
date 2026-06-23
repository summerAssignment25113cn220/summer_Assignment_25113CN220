#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter string: "; 
    cin >> str;

    int len = 0;
    while(str[len] != '\0') len++;

    char result = '\0';
    for(int i = 0; i < len; i++){
        for(int j = i + 1; j < len; j++){
            if(str[i] == str[j]){
                result = str[i];
                break;
            }
        }
        if(result) break;
    }

    if(result) cout << "First repeating : " << result << endl;
    else       cout << "No repeating character" << endl;
}