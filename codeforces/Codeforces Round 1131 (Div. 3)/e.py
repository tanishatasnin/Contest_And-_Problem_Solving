t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(abs(x) for x in a)
    negatives = sum(x < 0 for x in a)

    if negatives % 2 == 1:
        total -= 2 * min(abs(x) for x in a)

    print(total)