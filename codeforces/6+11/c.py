t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    if k == n:
        print("YES")
        print(*sorted(a[:k]))
        continue

    selected = a[:k]
    remaining = a[k:]

    if sum(selected) <= k * remaining[0]:
        print("NO")
        continue

    answer = sorted(selected) + remaining

    print("YES")
    print(*answer)