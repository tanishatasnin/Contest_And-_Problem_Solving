N, Q = map(int, input().split())
H = list(map(int, input().split()))
valley = [0] * (N + 1)

for i in range(2, N):
    if H[i - 2] > H[i - 1] < H[i]:
        valley[i] = 1

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + valley[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(prefix[R - 1] - prefix[L])