t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    answer = 2 ** (n - k + 1) + 2 * (k - 1)

    print(answer)