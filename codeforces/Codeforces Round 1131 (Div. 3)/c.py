t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(x == 1 for x in a):
        print(-1)
    elif any(x >= 2 for x in a[1:-1]):
        print(sum(a) - 1)
    else:
        print(sum(a) - (n - 1))