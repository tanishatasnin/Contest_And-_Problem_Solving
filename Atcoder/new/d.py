
import sys
input = sys.stdin.buffer.readline

N, M, K = map(int, input().split())
S = list(map(int, input().split()))
R = list(map(int, input().split()))

S.sort()
R.sort()
S = S[:N - K]

employee = 0
project = 0
answer = 0

for employee in range(len(S)):
    if project == M:
        break
    if S[employee] >= R[project]:
        answer += 1
        project += 1
print(answer)