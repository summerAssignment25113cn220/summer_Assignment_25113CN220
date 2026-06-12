#include<bits/stdc++.h>
using namespace std;

bool pal(int a){ 
    int og = a; int rev = 0;
    while(a > 0){
        rev = rev * 10 + a%10;
        a /= 10;
    } 
    if(rev == og ) return true;
    else{ return false;}
}
int main (){
    
    int n;
    cout << "enter a number : ";
    cin >> n;

    bool a = pal(n);
    if(a == true) cout << "palindrome";
    else{cout << "not a palindrome";}

}