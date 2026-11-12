t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    low = high = arr[0]
    ans = arr[0]

    for i in range(1, n):
        x = arr[i]

        ans = max(ans, x + max(abs(low), abs(high)))

        low = min(2 * low + x, low + x, x)
        high = max(2 * high + x, high + x, x)

    print(ans)