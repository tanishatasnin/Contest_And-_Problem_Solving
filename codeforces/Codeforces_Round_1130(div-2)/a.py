import sys
input = sys.stdin.readline

def val(a, k):
    s = set()
    r = []
    m = 0
    for x in a:
        s.add(x)
        while m in s:
            m += 1
        r.append(m)
    return sorted(r, reverse=True)[k - 1]

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    best = val(a, k)
    ans = -1
    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]
            x = val(a, k)
            if x > best:
                best = x
                ans = (i + 1, j + 1)
            a[i], a[j] = a[j], a[i]

    if ans == -1:
        print(-1)
    else:
        print(*ans)

    