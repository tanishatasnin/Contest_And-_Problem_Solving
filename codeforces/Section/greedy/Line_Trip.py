t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 2 * (x - a[-1])

    for i in range(1, n):
        ans = max(ans, a[i] - a[i - 1])

    ans = max(ans, a[0])

    print(ans)