n = int(input())
passengers = 0
capacity = 0
for _ in range(n):
    a, b = map(int, input().split())
    passengers -= a
    passengers += b
    capacity = max(capacity, passengers)
print(capacity)