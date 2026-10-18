n, m, k = map(int, input().split())
pieces = []

for _ in range(k):
    b, c = map(int, input().split())
    pieces.append((b, c))
pieces.sort(reverse=True)

total_cells = n * m
same_type_limit = (total_cells + 1) // 2
remaining = total_cells
answer = 0

for value, count in pieces:
    take = min(count, same_type_limit, remaining)
    answer += take * value
    remaining -= take
    if remaining == 0:
        break

print(answer)
