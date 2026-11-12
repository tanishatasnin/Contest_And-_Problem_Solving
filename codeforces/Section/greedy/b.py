t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    distinct = len(set(a))

    if n % 2 == 0:
        print(distinct)
    else:
        print(min(distinct, n - 1))