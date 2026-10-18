
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
        vector<int> sum(n - 4);
        vector<long long> freq(60001, 0);

        for (int i = 0; i < n - 4; i++) {
            sum[i] = a[i] + a[i + 2] - a[i + 4];
        }

        for (int i = 0; i < n - 4; i++) {
            int sum1 = sum[i];
            int id = sum1 + 30000;

            ans += freq[id];

            if (i >= 2 && sum[i - 2] == sum1) ans--;
            if (i >= 4 && sum[i - 4] == sum1) ans--;

            freq[id]++;
        }

        cout << ans << '\n';
    }

    return 0;
}
