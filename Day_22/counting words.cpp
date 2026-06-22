#include<bits/stdc++.h>
using namespace std; 

int main(){
    
    char str[200];
    cout << "Enter sentence: ";
    cin.getline(str, 200);  // getline reads full sentence with spaces

    int count = 0;
    int i = 0;

    while(str[i] != '\0'){
          if(str[i] == ' ' && str[i-1] != ' '){    // count a word when we hit a space after a nonspace element
            count++;
        }
        i++;
    }
        if(str[i-1] != ' ') count++;  // for counting the last word (no spaces after it)

    cout << "Word count = " << count << endl;
}
