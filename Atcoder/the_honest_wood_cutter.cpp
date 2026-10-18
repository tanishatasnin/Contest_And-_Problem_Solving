#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int A[200005], B[200005];

    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    for (int i = 1; i <= N; i++) {
        cin >> B[i];
    }

    for (int i = 1; i <= N; i++) {
        if (B[A[i]] != i) {
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;

    return 0;
}
