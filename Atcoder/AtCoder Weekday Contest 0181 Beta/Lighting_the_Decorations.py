n, m = map(int, input().split())

a = []
diff = [0] * (n + 2)

for _ in range(m):
    l, r = map(int, input().split())
    a.append((l, r))
    diff[l] += 1
    diff[r + 1] -= 1

cover = [0] * (n + 1)
one = [0] * (n + 1)

for i in range(1, n + 1):
    cover[i] = cover[i - 1] + diff[i]
    one[i] = one[i - 1] + (cover[i] == 1)

total = sum(x > 0 for x in cover)
answer = 0

for l, r in a:
    lost = one[r] - one[l - 1]
    answer = max(answer, total - lost)

print(answer)