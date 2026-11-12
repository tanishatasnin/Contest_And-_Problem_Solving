n, c = map(int, input().split())
a = list(map(int, input().split()))

current = 0
best = 0

for i in range(n):
    profit = a[i] - c

    current += profit

    best = max(best, current)

    if current < 0:
        current = 0

print(best)