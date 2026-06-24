#include<bits/stdc++.h>
using namespace std;

int main(){

    char sentence[200];
    cout << "enter a sentence : ";
    cin.getline(sentence, 200);

    char longest[100] = "";
    char current[100] = "";
    int  maxLen = 0, curLen = 0;

    int i = 0;
    while(sentence[i] != '\0'){
        if(sentence[i] != ' '){
            current[curLen] = sentence[i];
            curLen++;
        } else {
            current[curLen] = '\0';
            if(curLen > maxLen){
                maxLen = curLen;
                int k = 0;
                while(current[k] != '\0'){ longest[k] = current[k]; k++; }
                longest[k] = '\0';
            }
            curLen = 0;
        }
        i++;
    }
    // Checking last word
    current[curLen] = '\0';
    if(curLen > maxLen){
        int k = 0;
        while(current[k] != '\0'){ longest[k] = current[k]; k++; }
        longest[k] = '\0';
    }

    cout << "longest word found : " << longest << endl;
}