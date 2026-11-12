from collections import Counter

N = int(input())
count = Counter()

for _ in range(N):
    A, B = map(int, input().split())
    count[A - B] += 1

answer = 0

for frequency in count.values():
    answer += frequency * (frequency - 1) // 2

print(answer)