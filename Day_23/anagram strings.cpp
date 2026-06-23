#include<bits/stdc++.h>
using namespace std;

int main(){

    char s1[100], s2[100];
    cout << "enter string 1: "; cin >> s1;
    cout << "enter string 2: "; cin >> s2;

    int freq[26] = {0};  // frequency of each alphabet

    for(int i = 0; s1[i] != '\0'; i++)
        freq[s1[i] - 'a']++;

    for(int i = 0; s2[i] != '\0'; i++)
        freq[s2[i] - 'a']--;

    // if all zero → anagram
    bool isAnagram = true;                              // Anagram : same characters, different order
    for(int i = 0; i < 26; i++){                        // "listen" and "silent" are anagrams
        if(freq[i] != 0){ isAnagram = false; break; }
    }

    if(isAnagram) cout << "Anagram" << endl;
    else          cout << "Not Anagram" << endl;
}