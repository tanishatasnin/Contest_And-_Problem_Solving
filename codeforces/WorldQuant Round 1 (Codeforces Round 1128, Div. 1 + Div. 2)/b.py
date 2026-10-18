import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pref = [0] * (n + 1)
    suff = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] | a[i]
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1] | a[i]
    ans = pref[n]
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            continue
        j = i if a[i] < a[i + 1] else i + 1
        low = min(a[i], a[i + 1])
        high = max(a[i], a[i + 1])
        other = pref[j] | suff[j + 1]
        for x in range(low, high + 1):
            ans = max(ans, other | x)

    print(ans)