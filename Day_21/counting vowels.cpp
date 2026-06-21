#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "Enter a string: "; cin >> str;

    int vowels = 0, consonants = 0;

    for(int i = 0; str[i] != '\0'; i++){
        char ch = tolower(str[i]);       // convert to lowercase for easy check
        if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
            vowels++;
        else if(ch >= 'a' && ch <= 'z')
            consonants++;
    }

    cout << "Vowels = "     << vowels     << endl;
    cout << "Consonants = " << consonants << endl;
}