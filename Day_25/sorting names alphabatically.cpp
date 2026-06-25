#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "enter number of names : "; cin >> n;
    char names[n][50];

    for(int i = 0; i < n; i++){
        cout << "Enter name " << i+1 << ": ";
        cin >> names[i];
    }

    // Bubble sorting the names
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - i - 1; j++){
            
            // Comparing names character by character
            int k = 0;
            while(names[j][k] != '\0' && names[j+1][k] != '\0'){
                if(names[j][k] > names[j+1][k]){
                    // Swap names
                    char temp[50];
                    int m = 0;
                    while(names[j][m] != '\0'){ temp[m] = names[j][m]; m++; }
                    temp[m] = '\0';
                    m = 0;
                    while(names[j+1][m] != '\0'){ names[j][m] = names[j+1][m]; m++; }
                    names[j][m] = '\0';
                    m = 0;
                    while(temp[m] != '\0'){ names[j+1][m] = temp[m]; m++; }
                    names[j+1][m] = '\0';
                    break;
                }
                else if(names[j][k] < names[j+1][k]) break;
                k++;
            }
        }
    }

    cout << "Sorted names :\n";
    for(int i = 0; i < n; i++) cout << names[i] << endl;
}