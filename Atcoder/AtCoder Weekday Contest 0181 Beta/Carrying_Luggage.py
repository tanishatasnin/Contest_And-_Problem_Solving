

n, c = map(int, input().split())
w = sorted(map(int, input().split()))

total = 0
cart = 0

for weight in w:
    if total + weight <= c:
        total += weight
        cart += 1
    else:
        break

print(min(n, cart + 1))