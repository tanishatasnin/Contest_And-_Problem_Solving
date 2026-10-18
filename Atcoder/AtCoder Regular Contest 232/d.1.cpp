
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD = 998244353;
ll C[205][205], A[105], B[105], H[105][105], dp[105][105];

ll mpow(ll a, ll b) {
    ll r = 1;
    for (; b; b >>= 1, a = a * a % MOD)
        if (b & 1) r = r * a % MOD;
    return r;
}

ll ways(int n, int m, int r) {
    int d = n - 2 * m + 1 + r;
    if (d < 0) return 0;
    ll s = 0;
    for (int j = 0; j <= min(r, d); j++)
        s = (s + C[r][j] * B[j] % MOD * H[m][d-j]) % MOD;
    return s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    ll K;
    cin >> N >> K;

    ll a = (K - 1) % MOD, b = (2 - K + MOD) % MOD;
    ll f[205], inv[205];
    f[0] = 1;

    for (int i = 1; i <= 2 * N + 2; i++)
        f[i] = f[i-1] * i % MOD;

    inv[2*N+2] = mpow(f[2*N+2], MOD-2);
    for (int i = 2*N+2; i; i--)
        inv[i-1] = inv[i] * i % MOD;

    for (int n = 0; n <= 2*N+2; n++)
        for (int r = 0; r <= n; r++)
            C[n][r] = f[n] * inv[r] % MOD * inv[n-r] % MOD;

    A[0] = B[0] = 1;
    for (int i = 1; i <= N; i++) {
        A[i] = A[i-1] * a % MOD;
        B[i] = B[i-1] * b % MOD;
    }

    for (int m = 1; m <= N; m++)
        for (int d = 0; d <= N; d++)
            for (int u = 0; u <= d; u++) {
                int v = d-u;
                ll x = C[m+u-1][u] * A[u] % MOD;
                ll y = m == 1 ? (v == 0) :
                       C[m+v-2][v] * (v & 1 ? MOD-1 : 1) % MOD;
                H[m][d] = (H[m][d] + x*y) % MOD;
            }

    for (int n = 1; n <= N; n++)
        for (int q = 0; q < n-1; q++) {
            ll s = K % MOD * C[n-1][q] % MOD * A[n-1-q] % MOD;
            for (int r = 0; r <= q; r++)
                s = (s + ways(n, q+1, r) * dp[q+1][r]) % MOD;
            dp[n][q] = s;
        }

    ll ans = 0;
    for (int q = 0; q < N; q++)
        ans = (ans + dp[N][q]) % MOD;

    cout << ans << '\n';
}
