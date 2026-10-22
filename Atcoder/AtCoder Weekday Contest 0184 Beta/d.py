N, W, K = map(int, input().split())
H = list(map(int, input().split()))

# Bitmask for the sections cleared by placing the plow at each position.
plow_masks = []

for i in range(N):
    left = max(0, i - (W - 1) // 2)
    right = min(N - 1, i + W // 2)

    mask = 0
    for j in range(left, right + 1):
        mask |= 1 << j

    plow_masks.append(mask)

# reachable[mask] indicates whether this union of cleared sections is possible.
reachable = [False] * (1 << N)
reachable[0] = True

for _ in range(K):
    next_reachable = reachable.copy()  # We may use fewer than K operations.

    for mask in range(1 << N):
        if not reachable[mask]:
            continue

        for plow_mask in plow_masks:
            new_mask = mask | plow_mask
            next_reachable[new_mask] = True

    reachable = next_reachable

# Calculate the snow remaining for every reachable cleared-section mask.
total_snow = sum(H)
answer = total_snow

for mask in range(1 << N):
    if not reachable[mask]:
        continue

    cleared_snow = 0
    for i in range(N):
        if mask & (1 << i):
            cleared_snow += H[i]

    answer = min(answer, total_snow - cleared_snow)

print(answer)