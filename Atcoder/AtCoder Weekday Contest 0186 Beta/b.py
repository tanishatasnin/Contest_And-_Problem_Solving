N, K = map(int, input().split())
A = list(map(int, input().split()))

find = 0
for i in range(N):
    if A[i] == K:
        find += 1

for i in range(N - 1):
    if (A[i] < K < A[i + 1]) or (A[i] > K > A[i + 1]):
        find += 1

print(find)