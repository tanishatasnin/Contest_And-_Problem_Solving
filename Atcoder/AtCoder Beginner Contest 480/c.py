N, K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

answer = 0
end = 0

for a in A:
    if a > T:
        break

    if a > end:
        needed = (a - end + K - 1) // K
        answer += needed
        end += needed * K

    end = max(end, a + K)

if end < T:
    needed = (T - end + K - 1) // K
    answer += needed

print(answer)