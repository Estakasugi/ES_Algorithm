#include <iostream>
using namespace std;

int peachEating (int n){
    if(n == 1) return 1;
    return (peachEating(n-1) + 1) * 2;
}

int main () {
    int try_three = peachEating(5);
    cout << try_three << endl;
    return 0;
}