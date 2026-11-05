H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

counts = [sum(S[i][j] == 'F' for i in range(H)) for j in range(W)]

print(counts.index(max(counts)) + 1)