#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int a[n];

    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int i = 0; i <= n-k; i++) {

        int b[n];

        // original array save
        for (int j = 0; j < n; j++)
            b[j] = a[j];

        // k elements sort
        sort(b + i, b + i + k);

        // check
        int yes = 1;

        for (int j = 1; j < n; j++) {
            if (b[j-1] > b[j])
                yes = 0;
        }

        if (yes == 1) {
            cout << "Yes";
            return 0;
        }
    }

    cout << "No";

    return 0;
}
