t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    x, y, z = sorted([a, b, c])

    print(min(y - x, z - y))