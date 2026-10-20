N, K = map(int, input().split())
snacks = []
for _ in range(N):
    A, B = map(int, input().split())
    snacks.append((B, A))

snacks.sort(reverse=True)
answer = 0
remaining = K
for B, A in snacks:
    count = min(A, remaining)
    answer += count * B
    remaining -= count

    if remaining == 0:
        break

if remaining > 0:
    print(-1)
else:
    print(answer)