#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[200];      
    cout << "enter string : ";
    cin.getline(str, 200);  

    char result[200];
    int pos = 0;

    for(int i = 0; str[i] != '\0'; i++){
        if(str[i] != ' '){                 // for copying only non-space characters
            result[pos] = str[i];
            pos++;
        }
    }
    result[pos] = '\0';          // ends the string

    cout << "string without the spaces : " << result << endl;
}