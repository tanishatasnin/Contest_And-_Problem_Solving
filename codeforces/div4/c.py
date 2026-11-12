from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)

    left = []
    right = []

    for value in sorted(count):
        left.append(value)                 
        right.extend([value]*(count[value] - 1))
    right.sort(reverse=True)
    result = left + right
    visible = n - sum(max(0, x - 2) for x in count.values())

    print(visible)
    print(*result)