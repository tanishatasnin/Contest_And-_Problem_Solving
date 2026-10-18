
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        long long ans = 0;

        for (int i = 0; i <n-4 ; i++) {
            int sum1 = a[i] + a[i + 2] - a[i + 4];

            for (int j = i + 1; j <n-4 ; j++) {
                int sum2 = a[j] + a[j + 2] - a[j + 4];

                if (sum1 == sum2 &&
                    j != i + 2 &&
                    j != i + 4) {
                    ans++;
                }
            }
        }

        cout << ans << '\n';
    }

    return 0;
}
