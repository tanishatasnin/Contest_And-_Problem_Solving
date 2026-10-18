#include <iostream>
using namespace std;

int main() {
    int n, g;   // n=person , g=grapes
    cin >> n >> g;  // let , n=3 , g=5
    int each = g / n;   // each person = 5/3
    int extra = g % n;  // extra=  5%3 =2
    for (int i = 0; i < n; i++) {
    if (i < extra)
        cout << each + 1 << " ";
    else
        cout << each << " ";

    }
    return 0 ;
}
