N, K = map(int, input().split())
S = input()

ans = 0
for part in S.split('#'):
    if part and len(part) < K:
        print(-1)
        break
    ans += (len(part) + K - 1) // K
else:
    print(ans)