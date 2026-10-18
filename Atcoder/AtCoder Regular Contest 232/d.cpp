
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 998244353;
const int MAXN = 205;

ll fact[MAXN], invfact[MAXN];
ll C[MAXN][MAXN];
ll coef[MAXN][MAXN];
ll pwA[MAXN], pwB[MAXN];
ll dp[105][105];

ll modpow(ll a, ll b) {
    ll res = 1;
    while (b > 0) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

ll comb(int n, int r) {
    if (n < 0 || r < 0 || r > n) return 0;
    return C[n][r];
}

// Number of original sequences of length n
// that produce a fixed sequence of length m
// having r equal adjacent pairs.
ll ways(int n, int m, int r) {
    int d = n - 2 * m + 1 + r;
    if (d < 0) return 0;

    ll ans = 0;
    for (int j = 0; j <= min(r, d); j++) {
        ll term = comb(r, j) * pwB[j] % MOD;
        term = term * coef[m][d - j] % MOD;
        ans = (ans + term) % MOD;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll K;
    cin >> N >> K;

    ll a = (K - 1 + MOD) % MOD;
    ll b = (1 - a + MOD) % MOD;

    // Binomial coefficients
    fact[0] = 1;
    for (int i = 1; i <= 2 * N + 2; i++)
        fact[i] = fact[i - 1] * i % MOD;

    invfact[2 * N + 2] =
        modpow(fact[2 * N + 2], MOD - 2);

    for (int i = 2 * N + 1; i >= 0; i--)
        invfact[i] = invfact[i + 1] * (i + 1) % MOD;

    for (int n = 0; n <= 2 * N + 2; n++) {
        for (int r = 0; r <= n; r++) {
            C[n][r] = fact[n] * invfact[r] % MOD
                    * invfact[n - r] % MOD;
        }
    }

    pwA[0] = pwB[0] = 1;
    for (int i = 1; i <= N; i++) {
        pwA[i] = pwA[i - 1] * a % MOD;
        pwB[i] = pwB[i - 1] * b % MOD;
    }

    // coef[m][d] is the coefficient of z^d in
    // 1 / ((1 - (K-1)z)^m * (1+z)^(m-1)).
    for (int m = 1; m <= N; m++) {
        for (int d = 0; d <= N; d++) {
            ll sum = 0;

            for (int u = 0; u <= d; u++) {
                int v = d - u;

                ll left = comb(m + u - 1, u)
                        * pwA[u] % MOD;

                ll right;
                if (m == 1) {
                    right = (v == 0 ? 1 : 0);
                } else {
                    right = comb(m + v - 2, v);
                    if (v & 1) right = (MOD - right) % MOD;
                }

                sum = (sum + left * right) % MOD;
            }

            coef[m][d] = sum;
        }
    }

    // DP by sequence length
    for (int n = 1; n <= N; n++) {
        dp[n][n - 1] = 0;

        for (int q = 0; q < n - 1; q++) {
            // Number of non-constant sequences with q equal pairs
            ll total = K * comb(n - 1, q) % MOD;
            total = total * pwA[n - 1 - q] % MOD;

            // Add the scores of their resulting sequences
            int m = q + 1;

            for (int r = 0; r < m; r++) {
                ll w = ways(n, m, r);
                total = (total + w * dp[m][r]) % MOD;
            }

            dp[n][q] = total;
        }
    }

    ll ans = 0;
    for (int q = 0; q < N; q++)
        ans = (ans + dp[N][q]) % MOD;

    cout << ans << '\n';
    return 0;
}
