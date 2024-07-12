#include <iostream>
#include <array>
using namespace std;

// int springBounce (int n, int arr[], int l){
//     if( (arr[0] + 1) > l ) return 1;
//     return springBounce ( n-arr[0], arr[arr[0]..arr[l]], )
// }

int main () {
    
    int mySpring[] = { 1, 2, 3, 1, 2 };
    int length = sizeof(mySpring) / sizeof(mySpring[0]);
    
    int ans = mySpring[0:1];
    // int ans = springBounce( 5, mySpring, length);


    cout << ans << endl;
    return 0;
}