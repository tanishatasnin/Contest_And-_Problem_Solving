#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, v;
    cin >> n >> v;

    int h[n];

    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }

    int count_h = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {

                if ((i + 1) + (j + 1) + (k + 1) <= v) {
                    count_h = max(count_h, h[i] + h[j] + h[k]);
                }

            }
        }
    }

    cout << count_h << endl;
}
