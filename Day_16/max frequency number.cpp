#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cout << "Enter size: ";
    cin >> n;

    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    int maxfreq = 0, maxElem = arr[0];

    for(int i = 0; i < n; i++){
        int count = 0;
        for(int j = 0; j < n; j++){
            if(arr[j] == arr[i]) count++;
        }
        if(count > maxfreq){
            maxfreq = count;
            maxElem = arr[i];
        }
    }

    cout << "max frequency element = " << maxElem << endl;
    cout << "frequency = " << maxfreq << endl;
}