t = int(input())

for _ in range(t):
    n = int(input())
    a, b, c = map(int, input().split())
    weakest = min(a, b, c)
    print(n - weakest) ;