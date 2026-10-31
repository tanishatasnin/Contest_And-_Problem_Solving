t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    median = a[n // 2]

    cost = sum(abs(x - median) for x in a)
    operations = a[-1] - a[0]

    print(cost, operations)