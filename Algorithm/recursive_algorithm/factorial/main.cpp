#include <iostream>
using namespace std;

int facTorial (int n){
    if (n == 1) return 1;
    return facTorial(n-1) * n;
}

int main () {
    int try_three = facTorial(3);
    cout << try_three << endl;
    return 0;
}