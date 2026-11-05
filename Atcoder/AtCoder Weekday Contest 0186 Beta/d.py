from collections import deque

N, M, S, T = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)

d = [10**9] * (N + 1)
d[S] = 0
q = deque([S])
while q:
    v = q.popleft()
    first = min(g[v]) if g[v] else -1
    for u in g[v]:
        w = u != first
        if d[u] > d[v] + w:
            d[u] = d[v] + w
            if w:
                q.append(u)
            else:
                q.appendleft(u)
print(-1 if d[T] == 10**9 else d[T])