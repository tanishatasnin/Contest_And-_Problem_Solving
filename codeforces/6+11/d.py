import sys

N = 100005
p = [1] * N
p[0] = p[1] = 0

for i in range(2, 317):
    if p[i]:
        for j in range(i * i, N, i):
            p[j] = 0

for _ in range(int(input())):
    n = int(input())
    ans = []

    for x in map(int, input().split()):
        while not p[x]:
            x += 1
        ans.append(x)

    print(*ans)