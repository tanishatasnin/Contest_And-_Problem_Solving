t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    values = []
    for power in a:
        values.append(1 << power)   # for 2 ** power
    values.sort(reverse=True)

    x = 0  #initially
    y = 0

    for value in values:
        if x <= y:
            x += value
        else:
            y += value

    print(x * y)