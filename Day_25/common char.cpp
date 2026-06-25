#include<bits/stdc++.h>
using namespace std;

int main(){

    char s1[100], s2[100];
    cout << "enter string 1: "; cin >> s1;
    cout << "enter string 2: "; cin >> s2;

    cout << "Common characters : ";
    bool printed[256] = {false};

    for(int i = 0; s1[i] != '\0'; i++){
        for(int j = 0; s2[j] != '\0'; j++){
            if(s1[i] == s2[j] && !printed[(int)s1[i]]){
                cout << s1[i] << " ";
                printed[(int)s1[i]] = true;
            }
        }
    }
    cout << endl;
}