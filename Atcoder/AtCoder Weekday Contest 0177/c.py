import sys

input = sys.stdin.buffer.readline

n, k = map(int, input().split())
cost = list(map(int, input().split()))
parents_input = list(map(int, input().split()))
parent = [0] * (n + 1)

for city in range(2, n + 1):
    parent[city] = parents_input[city - 2]
targets = list(map(int, input().split()))
needed = bytearray(n + 1)

for city in targets:
    needed[city] = 1

answer = 0
for city in range(n, 1, -1):
    if needed[city]:
        answer += cost[city - 1]
        needed[parent[city]] = 1
if needed[1]:
    answer += cost[0]

print(answer) 