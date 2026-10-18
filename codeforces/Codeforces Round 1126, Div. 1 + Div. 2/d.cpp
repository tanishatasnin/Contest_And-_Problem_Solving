#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        long long k;
        cin >> n >> k;

        if (k < 0) {
            cout << -1 << '\n';
            return 0;
        }

        multiset<int> s;

        while (n--) {
            int x;
            cin >> x;
            s.insert(x);
        }

        long long ans = 0;

        while (!s.empty()) {
            int x = *s.begin();
            s.erase(s.begin());

            if (x > k) {
                s.insert((x + 1) / 2);
                s.insert((x + 1) / 2);
            }

            k++;
            ans++;
        }

        cout << ans << '\n';
    }
}
