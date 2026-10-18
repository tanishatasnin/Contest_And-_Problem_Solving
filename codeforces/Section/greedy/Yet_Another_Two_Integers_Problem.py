import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    difference = abs(a - b)

    print((difference + 9) // 10)