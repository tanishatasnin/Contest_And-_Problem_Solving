from collections import Counter

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = input().strip()
    q = input().strip()

    remaining = Counter(p) - Counter(q)

    if Counter(q) <= Counter(p) and remaining == Counter("six"):
        print("YES")
    else:
        print("NO")