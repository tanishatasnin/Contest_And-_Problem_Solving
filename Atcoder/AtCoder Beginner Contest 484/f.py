import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**18
size = 1
while size < N:
    size *= 2

mn = [INF] * (2 * size)
mx = [-INF] * (2 * size)
for i in range(N):
    if A[i] != -1:
        mn[size + i] = A[i]
        mx[size + i] = A[i]

for i in range(size - 1, 0, -1):
    mn[i] = min(mn[2 * i], mn[2 * i + 1])
    mx[i] = max(mx[2 * i], mx[2 * i + 1])


def update(pos, value):
    pos += size

    if value == -1:
        mn[pos] = INF
        mx[pos] = -INF
    else:
        mn[pos] = value
        mx[pos] = value

    pos //= 2
    while pos:
        mn[pos] = min(mn[2 * pos], mn[2 * pos + 1])
        mx[pos] = max(mx[2 * pos], mx[2 * pos + 1])
        pos //= 2


def query(left, right):
    left += size
    right += size
    minimum = INF
    maximum = -INF

    while left <= right:
        if left % 2 == 1:
            minimum = min(minimum, mn[left])
            maximum = max(maximum, mx[left])
            left += 1
        if right % 2 == 0:
            minimum = min(minimum, mn[right])
            maximum = max(maximum, mx[right])
            right -= 1

        left //= 2
        right //= 2
    return minimum, maximum


for _ in range(Q):
    query_type, x, y = map(int, input().split())
    if query_type == 1:
        update(x - 1, y)
    else:
        minimum, maximum = query(x - 1, y - 1)
        if minimum == INF or minimum == maximum:
            print("Yes")
        else:
            print("No")