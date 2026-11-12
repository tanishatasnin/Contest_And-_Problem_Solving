t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * n
    wi = 0
    total = 0

    for i in range(n - 1, -1, -1):
        x[i] = (a[i] + wi) & 1
        total ^= x[i]
        wi ^= x[i]
        if i + k < n:
            wi ^= x[i + k]

    print("Alice" if total else "Bob")