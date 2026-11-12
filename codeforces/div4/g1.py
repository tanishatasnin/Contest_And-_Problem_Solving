t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    def check(x):
        b = h * 3
        y = b[:]
        for i in range(1, 3 * n):
            y[i] = max(y[i], y[i - 1] - x)
        for i in range(3 * n - 2, -1, -1):
            y[i] = max(y[i], y[i + 1] - x)

        cost = 0
        for i in range(n, 2 * n):
            cost += y[i] - h[i - n]
            if cost > k:
                return False
        return True

    low = 0
    high = max(h) - min(h)
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1

    print(low)
