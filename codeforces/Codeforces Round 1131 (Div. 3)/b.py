t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    n = x + y + z

    if x >= y:
        print("P" * n)
    elif y >= z:
        print("R" * n)
    else:
        print("S" * n)