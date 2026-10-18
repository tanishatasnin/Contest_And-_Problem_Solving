
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int money;
    cin >> money;

    sort(a, a + n, greater<int>());

    int coin = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] <= money) {
            coin += money / a[i];
            money %= a[i];
        }
    }

    cout << coin << '\n';

    return 0;
}
