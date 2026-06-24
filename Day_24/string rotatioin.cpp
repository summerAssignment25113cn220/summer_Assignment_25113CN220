#include<bits/stdc++.h>
using namespace std;

int main(){

    char s1[100], s2[100];
    cout << "enter string 1: "; cin >> s1;
    cout << "enter string 2: "; cin >> s2;

    // Concatenate s1 with itself
    char doubled[200];
    int i = 0, j = 0;
    while(s1[i] != '\0') doubled[i] = s1[i++];
    while(s1[j] != '\0') doubled[i++] = s1[j++];
    doubled[i] = '\0';

    // Checking if s2 is a substring of doubled
    bool found = false;
    int len2 = 0;
    while(s2[len2] != '\0') len2++;

    for(int k = 0; doubled[k] != '\0'; k++){
        bool match = true;
        for(int m = 0; m < len2; m++){
            if(doubled[k+m] != s2[m]){ match = false; break; }
        }
        if(match){ found = true; break; }
    }

    if(found) cout << "Is a rotation" << endl;
    else      cout << "Not a rotation" << endl;
}
// "abcde" rotated → "cdeab" (rotate left by 2)
// Trick: if s2 is rotation of s1, then s2 will appear in s1+s1