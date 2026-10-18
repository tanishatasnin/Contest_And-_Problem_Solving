#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int n, k;
        cin >> n >> k;

        vector<int> cnt(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            ++cnt[x];
        }

        int x = 0;
        while (x <= n && cnt[x] >= 2 * k) {
            ++x;
        }
        cout << (cnt[x] == 2 * k - 1 ? "YES\n" : "NO\n");
    }

    return 0;
}
