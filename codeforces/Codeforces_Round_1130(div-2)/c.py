import sys
input = sys.stdin.readline

def possible(a, x, k):
    single = []
    n = len(a)
    for i in range(n):
        left = i == 0 or a[i] - a[i - 1] > k
        right = i == n - 1 or a[i + 1] - a[i] > k
        if left and right:
            single.append(a[i])
    used = 0
    i = 0

    while i < len(single):
        used += 1
        limit = single[i] + 2 * k
        i += 1
        while i < len(single) and single[i] <= limit:
            i += 1
    return used <= x

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    lo, hi = 1, 10**9
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(a, x, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)