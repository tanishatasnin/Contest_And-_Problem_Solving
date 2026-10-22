N = int(input())
S = input().strip()

groups = 0

for i in range(N):
    if S[i] == '#' and (i == 0 or S[i - 1] == '.'):
        groups += 1

print(groups)