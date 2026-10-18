from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))

prefix = [0] * (N + 1)

for i in range(N):
    prefix[i + 1] = prefix[i] + A[i]

end = [0] * (N + 1)

for i in range(1, N + 1):
    end[i] = i * (i + 1) // 2

block_sum = [0] * (N + 1)

for i in range(1, N + 1):
    block_sum[i] = block_sum[i - 1] + prefix[i]


def prefix_sum(x):
    """
    Returns B[1] + B[2] + ... + B[x]
    """

    if x <= 0:
        return 0
    block = bisect_right(end, x) - 1
    remaining = x - end[block]
    return block_sum[block] + prefix[remaining]


for _ in range(Q):
    L, R = map(int, input().split())

    answer = prefix_sum(R) - prefix_sum(L - 1)
    print(answer)