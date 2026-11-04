import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    values = sorted(freq)
    best = max(freq.values())

    for p in values:
        if best == n:
            break
        kept = 0
        for x in values:
            if x < p:
                continue
            if x % p == 0:
                kept += freq[x]

        best = max(best, kept)

    print(n - best)