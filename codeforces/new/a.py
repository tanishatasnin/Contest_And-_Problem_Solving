import sys

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    total = (l + r) * (r - l + 1) // 2
    erased = 0
    while l < r and (total < l or total > r):
        if total < l:
            total -= l
            l += 1
        else:
            total -= r
            r -= 1
        erased += 1

    print(erased)