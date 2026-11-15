from bisect import bisect_left, bisect_right

n, L, R = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0]
for x in a:
    prefix.append(prefix[-1] + x)

values = sorted(prefix)

bit = [0] * (n + 2)

def add(i):
    i += 1
    while i <= n + 1:
        bit[i] += 1
        i += i & -i

def get(i):
    result = 0
    i += 1
    while i > 0:
        result += bit[i]
        i -= i & -i
    return result

answer = 0

for p in prefix:
    left = p - R
    right = p - L

    l = bisect_left(values, left)
    r = bisect_right(values, right) - 1

    if l <= r:
        answer += get(r) - (get(l - 1) if l > 0 else 0)

    add(bisect_left(values, p))

print(answer)