#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int p = 1;
        while (p <= n) {
            p *= 2;
        }


        cout << 2 * p - 1 << '\n';

        int previous = 0;
        bool first = true;

        for (int i= 0; i < 2; i++) {
            for (int j = 0; j < p; j++) {
                int current = j ^ (j >> 1);

                if (!first) {
                    cout << (previous^current) << ' ';
                }

                previous = current;
                first = false;
            }
        }

        cout << '\n';
    }

    return 0;
}
