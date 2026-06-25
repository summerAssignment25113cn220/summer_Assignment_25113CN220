#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cout << "Enter number of words: "; cin >> n;
    char words[n][50];
    int  lens[n];

    for(int i = 0; i < n; i++){
        cout << "Enter word " << i+1 << ": ";
        cin >> words[i];
        int len = 0;
        while(words[i][len] != '\0') len++;
        lens[i] = len;
    }

    // Bubble sorting by length
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - i - 1; j++){
            if(lens[j] > lens[j+1]){
                // Swap words
                char temp[50];
                int  tempLen = lens[j];
                int  k = 0;
                while(words[j][k] != '\0'){ temp[k] = words[j][k]; k++; }
                temp[k] = '\0';
                k = 0;
                while(words[j+1][k] != '\0'){ words[j][k] = words[j+1][k]; k++; }
                words[j][k] = '\0';
                k = 0;
                while(temp[k] != '\0'){ words[j+1][k] = temp[k]; k++; }
                words[j+1][k] = '\0';
                lens[j]   = lens[j+1];
                lens[j+1] = tempLen;
            }
        }
    }

    cout << "Words sorted by length :\n";
    for(int i = 0; i < n; i++) cout << words[i] << endl;
}