import sys

input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

need = [0] * (N + 1)
stack = []

for a, b in zip(A, B):
    need[b] += 1
    while stack and need[stack[-1]] > 0:
        need[stack.pop()] -= 1
    stack.append(a)
    while stack and need[stack[-1]] > 0:
        need[stack.pop()] -= 1

print("Yes" if not stack else "No")