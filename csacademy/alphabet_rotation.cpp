
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct SegmentTree {
    int n;
    vector<ll> tree;

    SegmentTree(vector<ll>& a) {
        n = a.size();
        tree.assign(4 * max(1, n), 0);
        if (n > 0)
            build(1, 0, n - 1, a);
    }

    void build(int node, int l, int r, vector<ll>& a) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }

        int mid = (l + r) / 2;
        build(node * 2, l, mid, a);
        build(node * 2 + 1, mid + 1, r, a);

        tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
    }

    int findLast(int node, int l, int r, int ql, int qr, ll val) {
        if (r < ql || l > qr || tree[node] < val)
            return -1;

        if (l == r)
            return l;

        int mid = (l + r) / 2;

        int ans = findLast(node * 2 + 1, mid + 1, r, ql, qr, val);

        if (ans == -1)
            ans = findLast(node * 2, l, mid, ql, qr, val);

        return ans;
    }

    int findFirst(int node, int l, int r, int ql, int qr, ll val) {
        if (r < ql || l > qr || tree[node] < val)
            return -1;

        if (l == r)
            return l;

        int mid = (l + r) / 2;

        int ans = findFirst(node * 2, l, mid, ql, qr, val);

        if (ans == -1)
            ans = findFirst(node * 2 + 1, mid + 1, r, ql, qr, val);

        return ans;
    }

    int last(int l, int r, ll val) {
        if (n == 0 || l > r)
            return -1;
        return findLast(1, 0, n - 1, l, r, val);
    }

    int first(int l, int r, ll val) {
        if (n == 0 || l > r)
            return -1;
        return findFirst(1, 0, n - 1, l, r, val);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<pair<ll, ll>> platforms(N);

    for (int i = 0; i < N; i++)
        cin >> platforms[i].first >> platforms[i].second;

    vector<ll> x(M);

    for (int i = 0; i < M; i++)
        cin >> x[i];

    sort(x.begin(), x.end());

    vector<ll> gaps;

    for (int i = 0; i + 1 < M; i++)
        gaps.push_back(x[i + 1] - x[i]);

    SegmentTree st(gaps);

    ll ans = 0;

    for (int i = 0; i < N; i++) {
        ll l = platforms[i].first;
        ll r = platforms[i].second;
        ll len = r - l;

        int k = upper_bound(x.begin(), x.end(), l) - x.begin();

        if (k == M || x[k] >= r)
            continue;

        int prev = st.last(0, k - 1, len);
        int next = st.first(k, M - 2, len);

        int start = (prev == -1 ? 0 : prev + 1);
        int finish = (next == -1 ? M - 1 : next);

        ll leftPos = x[start] - len;
        ll rightPos = x[finish];

        ans += min(l - leftPos, rightPos - l);
    }

    cout << ans << '\n';

    return 0;
}