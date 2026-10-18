#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    string s[10000];

    for (int i = 0; i < n; i++) {
        cin >> s[i];
        sort(s[i].begin(), s[i].end());
    }



    int ans = 0;

    for (int i = 0; i < n; i++) {
        int count = 0;

        for (int j = 0; j < n; j++) {
            if (s[i] == s[j]) {
                count++;
            }
        }

        ans = max(ans, count);
    }

    cout << ans << endl;

    return 0;
}
