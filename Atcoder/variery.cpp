

#include <bits/stdc++.h>
using namespace std;

struct Gem {
    int color;
    long long value;
};

Gem a[200005];
bool used[200005];

bool cmp(Gem x, Gem y) {
    return x.value > y.value;
}

int main() {
    int N, K, M;
    cin >> N >> K >> M;

    for (int i = 0; i < N; i++) {
        cin >> a[i].color >> a[i].value;
    }

    sort(a, a + N, cmp);

    long long sum = 0;
    int colors = 0;

    for (int i = 0; i < K; i++) {
        sum += a[i].value;

        if (!used[a[i].color]) {
            used[a[i].color] = true;
            colors++;
        }
    }

    cout << sum << endl;
    return 0;
}
