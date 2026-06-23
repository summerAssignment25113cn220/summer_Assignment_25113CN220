#include<bits/stdc++.h>
using namespace std;

int main(){

    char str[100];
    cout << "enter string : "; 
    cin >> str;

    int freq[26] = {0};
    for(int i = 0; str[i] != '\0'; i++)
        freq[str[i] - 'a']++;

    int maxFreq = 0, maxIdx = 0;
    for(int i = 0; i < 26; i++){
        if(freq[i] > maxFreq){
            maxFreq = freq[i];
            maxIdx  = i;
        }
    }

    cout << "Max occurring char : " << (char)('a' + maxIdx) << endl;
    cout << "Frequency: " << maxFreq << endl;
}
// "aabbbbcc" → 'b' with frequency 4