
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        int V = N + 1;
        vector<vector<pair<int, int>>> adj(V);

        for (int i = 1; i <= N; i++) {
            adj[i - 1].push_back({i, 1});
            adj[i].push_back({i - 1, 0});
        }

        for (int i = 0; i < M; i++) {
            int L, R;
            cin >> L >> R;
            adj[L - 1].push_back({R, 2});
            adj[R].push_back({L - 1, -2});
        }

        vector<long long> dist(V, 0);
        vector<int> cnt(V, 0);
        vector<bool> inq(V, true);
        deque<int> q;

        for (int i = 0; i < V; i++)
            q.push_back(i);

        bool ok = true;

        while (!q.empty() && ok) {
            int u = q.front();
            q.pop_front();
            inq[u] = false;

            for (auto [v, w] : adj[u]) {
                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    cnt[v] = cnt[u] + 1;

                    if (cnt[v] >= V) {
                        ok = false;
                        break;
                    }

                    if (!inq[v]) {
                        if (!q.empty() && dist[v] < dist[q.front()])
                            q.push_front(v);
                        else
                            q.push_back(v);

                        inq[v] = true;
                    }
                }
            }
        }

        cout << (ok ? "Yes" : "No") << '\n';
    }

    return 0;
}
