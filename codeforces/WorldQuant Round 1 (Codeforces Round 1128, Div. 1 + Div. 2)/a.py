import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    positions = [i for i, ch in enumerate(s) if ch == '1']
    count = len(positions)

    if count == 1:
        answer = 0
    elif count == 2:
        answer = 1
    else:
        answer = positions[-1] - positions[0]

    print(answer)