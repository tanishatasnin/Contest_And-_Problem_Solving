import sys

input = sys.stdin.buffer.readline

N, M, T = map(int, input().split())

size = 1
while size < N:
    size *= 2

tree = [0] * (2 * size)
answer = [0] * N


def range_min(left, right):
    left += size
    right += size
    result = 10**18

    while left < right:
        if left & 1:
            result = min(result, tree[left])
            left += 1
        if right & 1:
            right -= 1
            result = min(result, tree[right])

        left //= 2
        right //= 2

    return result


def find_first(node, start, end, left, right, value):
    if end <= left or right <= start:
        return -1

    if left <= start and end <= right:
        if tree[node] != value:
            return -1

    if end - start == 1:
        return start

    mid = (start + end) // 2

    result = find_first(node * 2, start, mid, left, right, value)

    if result == -1:
        result = find_first(node * 2 + 1, mid, end, left, right, value)

    return result


def add_one(pos):
    pos += size
    tree[pos] += 1
    pos //= 2

    while pos:
        tree[pos] = min(tree[pos * 2], tree[pos * 2 + 1])
        pos //= 2


for _ in range(M):
    S, L, R = map(int, input().split())
    L -= 1

    minimum = range_min(L, R)
    seat = find_first(1, 0, size, L, R, minimum)

    add_one(seat)

    brightness = max(100 - (T - S), 0)
    answer[seat] += brightness

print(*answer)