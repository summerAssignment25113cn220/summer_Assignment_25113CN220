#include<bits/stdc++.h>
using namespace std;

int main(){
    
    char str[100];
    cout << "Enter a lowercase string: "; cin >> str;

    for(int i = 0; str[i] != '\0'; i++){
        if(str[i] >= 'a' && str[i] <= 'z')
            str[i] = str[i] - 32;  // ASCII trick: 'a'-'A' = 32
          // 'a' = 97, 'A' = 65, difference = 32
          // so subtract 32 to convert lowercase → uppercase
    
        }

    cout << "Uppercase: " << str << endl;
}
